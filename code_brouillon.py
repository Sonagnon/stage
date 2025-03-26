#used by mge_binning*
def build_mge_depth(
    contigs_file: str,
    depth_file: str,
    mges_data: pd.DataFrame,
    mge_depth_file: str,
):
    """Build mge depth form the whole assembly depth file from metabat script.

    Parameters:
    -----------
    contigs_file : str
        Path to the temporary file containing the list of the mge contigs name
        in the same order as the depth file will be written.
    depth_file : str
        Path to the whole depth file from Metabat2 script.
    mges_data : pandas.DataFrame
        Table with the mge contig names as index and the detected bacterial
        bins as column.
    mge_depth_file : str
        Path to write the depth file with only the mge contigs depth.
    """

    # Import the whole depth file as dataframe.
    whole_depth = pd.read_csv(depth_file, sep="\t")

    # Extract contigs name list.
    mge_list = list(mges_data.Name)

    # Extract line of the mge contigs
    mask = []
    for i in whole_depth.contigName:
        if i in mge_list:
            mask.append(True)
        else:
            mask.append(False)
    mge_depth = whole_depth.loc[mask]

    # Write the contigs list as the same order as the depth file.
    with open(contigs_file, "w") as f:
        for contig_name in mge_depth.contigName:
            f.write("%s\n" % contig_name)

    # Write mges depth file to use metabat2.
    mge_depth.to_csv(mge_depth_file, sep="\t", index=False) 


    #used by mge_binning*
def generate_mge_bins_metabat(
    mges_data: pd.DataFrame,
) -> pd.DataFrame:
    """Generates the binning of the mges contigs based on both HiC
    information (host detection) and the coverage and sequences information
    (metabat2 binning).

    Parameters:
    -----------
    mges_data : pandas.DataFrame
        Table with the contigs name as index and with information from both
        host detected from metator host and cluster form metabat2.

    Returns:
    --------
    pandas.DataFrame:
        Input table with the mge bin id column added.
    dict:
        Dictionary with the mge bin id as key and the list of the contigs
        name as value.
    """

    # Creates an unique ID for each future bin.
    mges_data["tmp"] = (
        mges_data.Host + "___" + list(map(str, mges_data.Metabat_bin))
    )

    # Create a new column with the bin id information added.
    bins_ids = {}
    mge_bins = {}
    mges_data["MetaTOR_MGE_bin"] = 0
    bin_id = 0
    for contig in mges_data.index:
        mge_id = mges_data.loc[contig, "tmp"]
        # Test if the mge id have been already seen.
        try:
            bin_id_old = bins_ids[mge_id]
            mges_data.loc[contig, "MetaTOR_MGE_bin"] = bin_id_old
            mge_bins[bin_id_old]["Contig"].append(
                mges_data.loc[contig, "Name"]
            )
        # Increment the bin id if it's the first time the mge id have been
        # seen.
        except KeyError:
            bin_id += 1
            bins_ids[mge_id] = bin_id
            mges_data.loc[contig, "MetaTOR_MGE_bin"] = bin_id
            mge_bins[bin_id]["Contig"] = [mges_data.loc[contig, "Name"]]
            mge_bins[bin_id]["Score"] = np.nan
    return mges_data, mge_bins


#used by mge_binning*
def run_metabat(
    contigs_file: str,
    input_fasta: str,
    outfile: str,
    mge_depth_file: str,
    temp_fasta: str,
) -> pd.DataFrame:
    """Function to launch metabat binning which is based on sequence and
    coverage information.

    Parameters:
    -----------
    contigs_file : str
        Path to the file with the list of the mges contigs in the same order
        as the depth file.
    input_fasta : str
        Path to the fasta containing the mges sequences. It could have more
        sequences.
    outfile : str
        Path to write the clustering results of metabat.
    mge_depth_file : str
        Path to the depth information of the mges file.
    temp_fasta : str
        Path to write a temporary fasta with the mges sequences in the same
        order as the depth file.

    Returns:
    --------
    pandas.DataFrame:
        Table with the mge contigs name as index and clustering result column.
    """

    # Extract fasta to have sequences at the same order as the depth file.
    cmd = "pyfastx extract {0} -l {1} > {2}".format(
        input_fasta, contigs_file, temp_fasta
    )
    process = sp.Popen(cmd, shell=True)
    process.communicate()

    # Run metabat2 without the bin output with no limit of bin size and save
    # cluster information in the output file.
    cmd = "metabat2 -i {0} -a {1} -o {2} -s 0 --saveCls --noBinOut".format(
        temp_fasta, mge_depth_file, outfile
    )
    process = sp.Popen(cmd, shell=True)
    process.communicate()

    # Import metabat result as a pandas dataframe and return it.
    metabat = pd.read_csv(
        outfile, sep="\t", index_col=False, names=["Name", "Metabat_bin"]
    )
    return metabat
