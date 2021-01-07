#!/usr/bin/env python3
# coding: utf-8
"""Alignement of reads

Align read files onto the assembly and return a 2D BED file with columns:
readIDA, contigA, posA, strandA, readIDB, contigB, posB, strandB. Reads are
mapped separately, sorted by names, then interleaved (rather than mapped in
paired-end mode) to capture the pairs mapping on two different contigs.

If the ligation sites are given, it will make an iteration on the unmapped, or
multi-mapped, cut them at the ligation site and try to align them again to
improve the numbers of reads uniquely mapped. However it's time consumming and
doesn"t improve a lot with short reads (35bp). 

This module contains all these alignment functions:
    - align
    - alignement
    - cutsite_trimming
    - merge_alignement
    - pairs_alignement
    - process_bamfile
    - trim_reads 
"""

import csv
import gzip
import os
import sys
import metator.io as mio
import pandas as pd
import pysam as ps
import subprocess as sp
from Bio import SeqIO
from metator.log import logger
from os.path import join


# TODO: Modify the cutsite trimming to try to map both part of the cut read.
# TODO: cutsite trimming in python language
# TODO: adpat trimmed reads
# TODO: Check description of the function


def align(fq_in, index, bam_out, n_cpu):
    """Alignment
    Aligns reads of fq_in with bowtie2. Parameters of bowtie2 are set as
    --very-sensitive-local

    Parameters
    ----------
    fq_in : str
        Path to input fastq file to align. If multiple files are given, list of
        path separated by a comma.
    index : str
        Path to the bowtie2 index genome.
    bam_out : str
        Path where the alignment should be written in BAM format.
    n_cpu : int
        The number of CPUs to use for the alignment.
    """

    # Align the reads on the reference genome
    map_args = {"cpus": n_cpu, "fq": fq_in, "idx": index, "bam": bam_out}
    cmd = (
        "bowtie2 -x {idx} -p {cpus} --quiet --very-sensitive-local {fq}"
    ).format(**map_args)

    map_process = sp.Popen(cmd, shell=True, stdout=sp.PIPE)
    sort_process = sp.Popen(
        "samtools sort -n -@ {cpus} -o {bam}".format(**map_args),
        shell=True,
        stdin=map_process.stdout,
    )
    out, err = sort_process.communicate()

    return 0


def merge_alignment(forward_aligned, reverse_aligned, out_file):
    """Merge forward and reverse alignment into one file with pairs which both
    reads are aligned on the genome. The final alignment  dataframe is written
    in the output file.

    Parameters
    ----------
    forward_alignement : pandas.core.frame.DataFrame
        Table containing the data of the forward reads kept after the alignment.
        With five columns: ReadID, Contig, Position_start, Position_end, strand.
    reverse_alignement : pandas.core.frame.DataFrame
        Table containing the data of the forward reads kept after the alignment.
        With five columns: ReadID, Contig, Position_start, Position_end, strand.
    out_file : str
        Path to write the output file.

    Return
    ------
    pandas.core.frame.DataFrame:
        Table conatining the alignement data of the pairs: ReadID, ContigA,
        Position_startA, Position_endA, StrandA, ContigB, Position_startB,
        Position_endB, StrandB
    """

    # Merge the two dataframe on the readID column
    pairs = pd.merge(forward_aligned, reverse_aligned, on=0, how="inner")

    logger.info("{0} pairs aligned.".format(len(pairs)))

    return pairs


def pairs_alignment(
    for_fq_in,
    rev_fq_in,
    min_qual,
    tmp_dir,
    ref,
    ligation_sites,
    out_file,
    n_cpu,
):
    """General function to do the whole alignement of both fastq.
    The Function write at the output file location given as an argument and
    return a 2D bed file of the aligned reads with 9 columns: ReadID, ContigA,
    Position_startA, Position_endA, StrandA, ContigB, Position_startB,
    Position_endB, StrandB

    Parameters
    ----------
    for_fq_in : str
        Path to input forward fastq file to align. If multiple files are given,
        list of path separated by a comma.
    rev_fq_in : str
        Path to input reverse fastq file to align. If multiple files are given,
        list of path separated by a comma.
    min_qual : int
        Minimum mapping quality required to keep Hi-C pairs.
    tmp_dir : str
        Path where temporary files should be written.
    ref : str
        Path to the index genome.
    ligation_sites : str
        The list of ligations site possible depending on the restriction enzymes
        used separated by a comma. Exemple of the ARIMA kit:
        GATCGATC,GANTGATC,GANTANTC,GATCANTC
    out_file : str
        Path to write the output file.
    n_cpu : int
        The number of CPUs to use for the alignment.

    Return
    ------
    pandas.core.frame.DataFrame:
        Table conatining the alignement data of the pairs: ReadID, ContigA,
        Position_startA, Position_endA, StrandA, ContigB, Position_startB,
        Position_endB, StrandB
    """

    # Counting reads forward and reverse reads
    total_reads_forward = 0
    with mio.read_compressed(for_fq_in) as inf:
        for _ in inf:
            total_reads_forward += 1
    total_reads_forward /= 4
    total_reads_reverse = 0
    with mio.read_compressed(rev_fq_in) as inf:
        for _ in inf:
            total_reads_reverse += 1
    total_reads_reverse /= 4

    # Safety check: Same numbers of reads in the forward and reverse fastq file.
    if total_reads_forward != total_reads_reverse:
        logger.warning(
            "Different numbers of forward and reverse reads. Please check if \
                your files are not corrupted"
        )

    logger.info(
        "{0} paired-end reads in the library.".format(total_reads_reverse)
    )

    # Throw error if index does not exist
    index = mio.check_fasta_index(ref, mode="bowtie2")
    if index is None:
        logger.error(
            "Reference index is missing, please build the bowtie2 index first."
        )
        sys.exit(1)

    # Create a temporary file to save the alignment.
    temp_alignment_for = join(tmp_dir, "temp_alignment_for.bam")
    temp_alignment_rev = join(tmp_dir, "temp_alignment_rev.bam")
    filtered_out_for = join(tmp_dir, "for_temp_alignment.bed")
    filtered_out_rev = join(tmp_dir, "rev_temp_alignment.bed")

    # If asked will digest the reads with the ligtion sites before
    # alignment.
    if isinstance(ligation_sites, str):

        # Create temporary file for the digested reads.
        temp_fq = join(tmp_dir, "digested_reads")

        # Create a temporary fastq with the trimmed reads at the ligation
        # sites.
        (for_fq_in, rev_fq_in,) = digest_ligation_sites(
            for_fq_in,
            rev_fq_in,
            ligation_sites,
            temp_fq,
        )

    # Align the forward reads
    align(for_fq_in, index, temp_alignment_for, n_cpu)

    # Filters the aligned and non aligned reads
    unaligned = process_bamfile(temp_alignment_for, min_qual, filtered_out_for)

    forward_aligned = pd.DataFrame(
        csv.reader(open(filtered_out_for), delimiter="\t")
    )

    # Align the reverse reads
    align(rev_fq_in, index, temp_alignment_rev, n_cpu)

    # Filters the aligned and non aligned reads
    unaligned = process_bamfile(temp_alignment_rev, min_qual, filtered_out_rev)

    reverse_aligned = pd.DataFrame(
        csv.reader(open(filtered_out_rev), delimiter="\t")
    )

    # Merge alignement to create a pairs file
    pairs = merge_alignment(forward_aligned, reverse_aligned, out_file)

    pairs.to_csv(out_file, sep="\t", index=False, header=False)

    return pairs


def process_bamfile(alignment, min_qual, filtered_out):
    """Filter alignment BAM files

    Reads all the reads in the input BAM alignment file. Keep reads in the
    output if they are aligned with a good quality saving their uniquely ReadID,
    Contig, Position_start, Position_end, strand to save memory. Otherwise add
    their name in a set to stage them in order to recuperate them if necessary.

    Parameters
    ----------
    temp_alignment : str
        Path to the input temporary alignment.
    min_qual : int
        Minimum mapping quality required to keep a Hi-C pair.
    filtered_out : str
        Path to the output temporary bed alignement.

    Returns
    -------
    pandas..core.frame.DataFrame:
        Table containing the data of the reads mapping unambiguously and with a
        mapping quality superior to the threshold given. Five columns: ReadID,
        Contig, Position_start, Position_end, strand
    set:
        Contains the names reads that did not align.
    """
    # Check the quality and status of each aligned fragment.
    # Write the ones with good quality in the aligned dataframe.
    # Keep ID of those that do not map unambiguously to be trimmed.

    aligned_reads = 0
    unaligned = set()
    temp_bam = ps.AlignmentFile(alignment, "rb", check_sq=False)
    f = open(filtered_out, "a")
    for r in temp_bam:
        if r.mapping_quality >= min_qual:
            if r.flag == 0:
                aligned_reads += 1
                read = str(
                    r.query_name
                    + "\t"
                    + r.reference_name
                    + "\t"
                    + str(r.reference_start)
                    + "\t"
                    + str(r.reference_end)
                    + "\t"
                    + "+\n"
                )
                f.write(read)
            elif r.flag == 16:
                aligned_reads += 1
                read = str(
                    r.query_name
                    + "\t"
                    + r.reference_name
                    + "\t"
                    + str(r.reference_start)
                    + "\t"
                    + str(r.reference_end)
                    + "\t"
                    + "-\n"
                )
                f.write(read)
            else:
                unaligned.add(r.query_name)
        else:
            unaligned.add(r.query_name)

    f.close()
    temp_bam.close()

    # Display alignement informations
    logger.info("{0} reads aligned.".format(aligned_reads))

    return unaligned


def digest_ligation_sites(fq_for, fq_rev, ligation_sites, output):
    """Create new reads to manage pairs with a digestion and create multiple
    pairs to take into account all the contact present.

    The function write two files for both the forward and reverse fastq with the
    new reads. The new reads have at the end of the ID ":1" added to
    differentiate the different pairs created from one read.

    To make the function faster, for each reads only the first site of ligation
    is kept and the algorithm stop to search for others sites as the probability
    is very low. We already have very few pairs with ligation sites in both
    reads.

    Parameters
    ----------
    fq_for : str
        Path to the forward fastq file to digest.
    fq_rev : str
        Path to the reverse fatsq file to digest.
    ligation_sites : str
        The list of ligations site possible depending on the restriction
        enzymes used separated by a comma. Exemple of the ARIMA kit:
        GATCGATC,GANTGATC,GANTANTC,GATCANTC
    output : str
        Path for the ouput file. The forward will have a suffix "_for.fq" and
        the reverse "_rev.fq".
    """

    # Process the ligation sites given
    ligation_sites = mio.process_ligation_sites(ligation_sites)

    # Create the two output file
    output_for = "{0}_for.fq".format(output)
    output_rev = "{0}_rev.fq".format(output)

    pair_reads = dict()
    # Read the forward file and detect the ligation sites.
    for read in SeqIO.parse(mio.read_compressed(fq_for), "fastq"):
        pair_reads[read.name] = {
            "for_seq": read.seq,
            "rev_seq": None,
            "for_qual": read.format("fastq").split("\n")[3],
            "rev_qual": None,
            "for_ls": None,
            "rev_ls": None,
        }
        for ls in ligation_sites:
            if ls in read.seq:
                pair_reads[read.name]["for_ls"] = read.seq.find(ls)
                break

    # Read the reverse file and detect the ligation sites.
    for read in SeqIO.parse(mio.read_compressed(fq_rev), "fastq"):
        # Sanity check if some reads are not present in the forward file
        if read.name in pair_reads:
            pair_reads[read.name]["rev_seq"] = read.seq
            pair_reads[read.name]["rev_qual"] = read.format("fastq").split(
                "\n"
            )[3]
            for ls in ligation_sites:
                if ls in read.seq:
                    pair_reads[read.name]["for_ls"] = read.seq.find(ls)
                    break

    # Cut and create new pairs.
    original_number_of_pairs = 0
    zero_site_pairs = 0
    one_site_pairs = 0
    two_site_pairs = 0
    for_fq = open(output_for, "w")
    rev_fq = open(output_rev, "w")
    for read in pair_reads:
        # Sanity check if there are no reverse read for the forward read.
        if pair_reads[read]["rev_seq"] != None:
            original_number_of_pairs += 1
            # Save the sequence and quality of the original pair.
            for_seq_0 = pair_reads[read]["for_seq"]
            for_qual_0 = pair_reads[read]["for_qual"]
            rev_seq_0 = pair_reads[read]["rev_seq"]
            rev_qual_0 = pair_reads[read]["rev_qual"]
            if pair_reads[read]["for_ls"] != None:
                # Truncate the forward pair. For the truncation as the enzymes
                # used in HiC have usually 8 base pairs long we choose these
                # size to truncate them.
                for_seq_1 = for_seq_0[: pair_reads[read]["for_ls"]]
                for_seq_2 = for_seq_0[pair_reads[read]["for_ls"] + 8 :]
                for_qual_1 = for_qual_0[: pair_reads[read]["for_ls"]]
                for_qual_2 = for_qual_0[pair_reads[read]["for_ls"] + 8 :]
                if pair_reads[read]["rev_ls"] != None:
                    # Truncate the reverse pair.
                    two_site_pairs += 1
                    rev_seq_1 = rev_seq_0[: pair_reads[read]["rev_ls"]]
                    rev_seq_2 = rev_seq_0[pair_reads[read]["rev_ls"] + 8 :]
                    rev_qual_1 = rev_qual_0[: pair_reads[read]["rev_ls"]]
                    rev_qual_2 = rev_qual_0[pair_reads[read]["rev_ls"] + 8 :]
                    # Write the 6 new pairs in case there are two ligation
                    # sites.
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", for_seq_1, for_qual_1)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", for_seq_1, for_qual_1)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", for_seq_1, for_qual_1)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":4", for_seq_2, for_qual_2)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":5", for_seq_2, for_qual_2)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":6", rev_seq_1, rev_qual_1)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", for_seq_2, for_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", rev_seq_1, rev_qual_1)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", rev_seq_2, rev_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":4", rev_seq_1, rev_qual_1)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":5", rev_seq_2, rev_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":6", rev_seq_2, rev_qual_2)
                    )
                else:
                    # Write the 3 new pairs in case there is one ligation site.
                    one_site_pairs += 1
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", for_seq_1, for_qual_1)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", for_seq_1, for_qual_1)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", for_seq_2, for_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", rev_seq_0, rev_qual_0)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", for_seq_2, for_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", rev_seq_0, rev_qual_0)
                    )
            else:
                if pair_reads[read]["rev_ls"] != None:
                    # Truncate the reverse pair.
                    one_site_pairs += 1
                    rev_seq_1 = rev_seq_0[: pair_reads[read]["rev_ls"]]
                    rev_seq_2 = rev_seq_0[pair_reads[read]["rev_ls"] + 8 :]
                    rev_qual_1 = rev_qual_0[: pair_reads[read]["rev_ls"]]
                    rev_qual_2 = rev_qual_0[pair_reads[read]["rev_ls"] + 8 :]
                    # Write the 3 new pairs in case there is one ligation site.
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", for_seq_0, for_qual_0)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", for_seq_0, for_qual_0)
                    )
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", rev_seq_1, rev_qual_1)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":1", rev_seq_1, rev_qual_1)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":2", rev_seq_2, rev_qual_2)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n"
                        % (read + ":3", rev_seq_2, rev_qual_2)
                    )
                else:
                    # Write the original pair if there is no ligation site.
                    zero_site_pairs += 1
                    for_fq.write(
                        "@%s\n%s\n+\n%s\n" % (read, for_seq_0, for_qual_0)
                    )
                    rev_fq.write(
                        "@%s\n%s\n+\n%s\n" % (read, rev_seq_0, rev_qual_0)
                    )
    rev_fq.close()
    for_fq.close()
    logger.info("Number of pairs: {0}".format(original_number_of_pairs))
    logger.info(
        "Number of pairs with no ligation site: {0}".format(zero_site_pairs)
    )
    logger.info(
        "Number of pairs with no ligation site: {0}".format(one_site_pairs)
    )
    logger.info(
        "Number of pairs with no ligation site: {0}".format(two_site_pairs)
    )
    return output_for, output_rev
