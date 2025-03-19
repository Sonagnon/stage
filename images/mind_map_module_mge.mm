<map version="freeplane 1.7.0">
<!--To view this file, download free mind mapping software Freeplane from http://freeplane.sourceforge.net -->
<node FOLDED="false" ID="ID_235634816" CREATED="1742380623348" MODIFIED="1742397191565" NodeVisibilityConfiguration="SHOW_HIDDEN_NODES"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <u><font size="4">function</font></u><br/><b><font size="3">mge_binning()</font></b>
    </p>
  </body>
</html>

</richcontent>
<hook NAME="MapStyle">
    <properties edgeColorConfiguration="#808080ff,#000000ff,#ff0033ff,#009933ff,#3333ffff,#ff6600ff,#cc00ccff,#ffbf00ff,#00ff99ff,#0099ffff,#996600ff,#000000ff,#cc0066ff,#33ff00ff,#ff9999ff,#0000ccff,#cccc00ff,#0099ccff,#006600ff,#ff00ccff,#00cc00ff,#0066ccff,#00ffffff" fit_to_viewport="false" show_note_icons="true" show_icon_for_attributes="true"/>

<map_styles>
<stylenode LOCALIZED_TEXT="styles.root_node" STYLE="oval" UNIFORM_SHAPE="true" VGAP_QUANTITY="24.0 pt" TEXT_SHORTENED="true">
<font SIZE="24"/>
<richcontent TYPE="DETAILS" LOCALIZED_HTML="styles_background_html"/>
<stylenode LOCALIZED_TEXT="styles.predefined" POSITION="right" STYLE="bubble">
<font SIZE="9"/>
<stylenode LOCALIZED_TEXT="default" ICON_SIZE="12.0 pt" COLOR="#000000" STYLE="bubble" SHAPE_VERTICAL_MARGIN="0.0 pt" TEXT_ALIGN="CENTER" MAX_WIDTH="120.0 pt" MIN_WIDTH="120.0 pt">
<font NAME="Arial" SIZE="9" BOLD="true" ITALIC="false"/>
<edge STYLE="bezier" WIDTH="3"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.details">
<font SIZE="11" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.attributes" COLOR="#000000" BACKGROUND_COLOR="#ffffff">
<font SIZE="9" BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.note" COLOR="#000000" BACKGROUND_COLOR="#ffffff" TEXT_ALIGN="LEFT">
<font BOLD="false"/>
</stylenode>
<stylenode LOCALIZED_TEXT="defaultstyle.floating">
<edge STYLE="hide_edge"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.user-defined" POSITION="right" STYLE="bubble">
<font SIZE="9"/>
<stylenode LOCALIZED_TEXT="styles.important">
<icon BUILTIN="yes"/>
<edge COLOR="#0000cc"/>
</stylenode>
</stylenode>
<stylenode LOCALIZED_TEXT="styles.AutomaticLayout" POSITION="right" STYLE="bubble">
<font SIZE="9"/>
<stylenode LOCALIZED_TEXT="AutomaticLayout.level.root" COLOR="#000000" STYLE="oval" UNIFORM_SHAPE="true" MAX_WIDTH="120.0 pt" MIN_WIDTH="120.0 pt">
<font SIZE="24" ITALIC="true"/>
<edge STYLE="bezier" WIDTH="3"/>
</stylenode>
</stylenode>
</stylenode>
</map_styles>
</hook>
<hook NAME="accessories/plugins/AutomaticLayout.properties" VALUE="ALL"/>
<font NAME="Noto Sans Georgian" BOLD="false" ITALIC="false"/>
<hook NAME="AutomaticEdgeColor" COUNTER="0" RULE="FOR_COLUMNS"/>
<attribute_layout NAME_WIDTH="102.74999693781146 pt" VALUE_WIDTH="102.74999693781146 pt"/>
<attribute NAME="checkv_db" VALUE=""/>
<attribute NAME="depth_file" VALUE=""/>
<attribute NAME="fasta_mges_contigs" VALUE=""/>
<attribute NAME="network" VALUE=""/>
<attribute NAME="contigs_data" VALUE=""/>
<attribute NAME="mges_list_id" VALUE=""/>
<attribute NAME="out_dir" VALUE=""/>
<attribute NAME="pairs_files" VALUE=""/>
<attribute NAME="tmp_dir" VALUE=""/>
<attribute NAME="threshold_bin" VALUE="0,8" OBJECT="org.freeplane.features.format.FormattedNumber|0.8"/>
<attribute NAME="threshold_asso" VALUE="0,1" OBJECT="org.freeplane.features.format.FormattedNumber|0.1"/>
<attribute NAME="association" VALUE="True/False"/>
<attribute NAME="plot" VALUE="True"/>
<attribute NAME="remove_tmp" VALUE="True"/>
<attribute NAME="threads" VALUE="1" OBJECT="org.freeplane.features.format.FormattedNumber|1"/>
<attribute NAME="method" VALUE="&quot;pairs&quot;"/>
<attribute NAME="random" VALUE="False"/>
<cloud COLOR="#f0f0f0" SHAPE="ARC"/>
<richcontent TYPE="DETAILS">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><font color="#008000"><b>main function of the mge module</b></font></i>
    </p>
  </body>
</html>

</richcontent>
<node TEXT="" POSITION="right" ID="ID_1981124004" CREATED="1742389820188" MODIFIED="1742389820192">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_1755645086" CREATED="1742381346236" MODIFIED="1742389750826"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <u>Function</u>
    </p>
    <p>
      run_checkv
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="checkv_db" VALUE=""/>
<attribute NAME="fasta" VALUE=""/>
<attribute NAME="out_dir" VALUE=""/>
<attribute NAME="remove_tmp" VALUE="True/False"/>
<attribute NAME="threads" VALUE="4" OBJECT="org.freeplane.features.format.FormattedNumber|4"/>
</node>
<node TEXT="" POSITION="right" ID="ID_150501646" CREATED="1742389820176" MODIFIED="1742389820186">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Output : out_dir" ID="ID_1389209361" CREATED="1742389820199" MODIFIED="1742395607885"/>
</node>
<node TEXT="" POSITION="right" ID="ID_1096294386" CREATED="1742389879911" MODIFIED="1742389879917">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_1282169008" CREATED="1742381427588" MODIFIED="1742396799093"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      shuffle_mge_bins()
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="mges_data" VALUE=""/>
<font NAME="DejaVu Sans"/>
</node>
<node TEXT="" POSITION="right" ID="ID_1635002288" CREATED="1742389879895" MODIFIED="1742389879907">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Outputs" ID="ID_1915667576" CREATED="1742389879923" MODIFIED="1742392663566">
<node TEXT="mges_data" ID="ID_964178215" CREATED="1742392019734" MODIFIED="1742392078858"/>
<node TEXT="mges_bins" ID="ID_408518168" CREATED="1742392065616" MODIFIED="1742392089943"/>
</node>
</node>
<node TEXT="" POSITION="right" ID="ID_1444314882" CREATED="1742390129470" MODIFIED="1742390129473">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_1015497632" CREATED="1742381530373" MODIFIED="1742394032911"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      generate_mge_bins_metabat()
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="mges_data" VALUE=""/>
</node>
<node TEXT="" POSITION="right" ID="ID_126601124" CREATED="1742390129457" MODIFIED="1742390129468">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Outputs" ID="ID_883841265" CREATED="1742390129475" MODIFIED="1742392670234">
<node TEXT=" mges_data" ID="ID_245936899" CREATED="1742392099432" MODIFIED="1742392128097"/>
<node ID="ID_891685746" CREATED="1742392106295" MODIFIED="1742395950103"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <font color="#99cc00">mge_bins</font>
    </p>
  </body>
</html>

</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_129136412" STARTINCLINATION="126;222;" ENDINCLINATION="329;39;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_611406252" STARTINCLINATION="324;60;" ENDINCLINATION="-283;51;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="" POSITION="right" ID="ID_917170833" CREATED="1742390307091" MODIFIED="1742390307095">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="Function&#xa;run_metabat" POSITION="right" ID="ID_325562749" CREATED="1742381475197" MODIFIED="1742393648764">
<attribute_layout NAME_WIDTH="77.24999769777067 pt"/>
<attribute NAME="contigs_file" VALUE=""/>
<attribute NAME="input_fasta" VALUE=""/>
<attribute NAME="outfile" VALUE=""/>
<attribute NAME="mge_depth_file" VALUE=""/>
<attribute NAME="temp_fasta" VALUE=""/>
</node>
<node TEXT="" POSITION="right" ID="ID_827239955" CREATED="1742390307084" MODIFIED="1742390307088">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Output : metabat (csv)" ID="ID_760830676" CREATED="1742390307098" MODIFIED="1742390322241"/>
</node>
<node TEXT="" POSITION="right" ID="ID_170054562" CREATED="1742388358543" MODIFIED="1742388358546">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_864822225" CREATED="1742381487885" MODIFIED="1742396299305"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      generate_mge_bins_pairs
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="mges_data" VALUE=""/>
<attribute NAME="pairs_files" VALUE=""/>
<attribute NAME="threshold" VALUE="0,8" OBJECT="org.freeplane.features.format.FormattedNumber|0.8"/>
<font NAME="Dialog"/>
<cloud COLOR="#f0f0f0" SHAPE="ARC"/>
<node TEXT="" ID="ID_1644141149" CREATED="1742387803203" MODIFIED="1742387803206">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="Function&#xa;update_mge_data()" ID="ID_190458994" CREATED="1742381501774" MODIFIED="1742388648572">
<attribute_layout NAME_WIDTH="66.74999801069504 pt" VALUE_WIDTH="66.74999801069504 pt"/>
<attribute NAME="bins" VALUE=""/>
<attribute NAME="mges_data" VALUE=""/>
</node>
<node TEXT="" ID="ID_556943461" CREATED="1742387803201" MODIFIED="1742387803203">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="outputs" ID="ID_1777302077" CREATED="1742387803208" MODIFIED="1742392041879">
<node TEXT=" mges_data" ID="ID_231695304" CREATED="1742391994126" MODIFIED="1742392014568"/>
<node TEXT="mge_bins" ID="ID_822171073" CREATED="1742392029127" MODIFIED="1742392048039"/>
</node>
</node>
<node TEXT="" ID="ID_438651577" CREATED="1742388085253" MODIFIED="1742388085254">
<hook NAME="FirstGroupNode"/>
</node>
<node TEXT="Function&#xa;resolve_matrix()" ID="ID_1224680280" CREATED="1742381509955" MODIFIED="1742388654984">
<attribute NAME="mat" VALUE=""/>
<attribute NAME="threshold" VALUE="0,8" OBJECT="org.freeplane.features.format.FormattedNumber|0.8"/>
</node>
<node TEXT="" ID="ID_428721879" CREATED="1742388085252" MODIFIED="1742388085253">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node ID="ID_1946720950" CREATED="1742388085257" MODIFIED="1742395223132"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      output : <font color="#0000ff">bins</font>
    </p>
  </body>
</html>

</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_190458994" STARTINCLINATION="-17;-283;" ENDINCLINATION="-234;-10;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
<node TEXT="" ID="ID_1977967385" CREATED="1742388205009" MODIFIED="1742388205011">
<hook NAME="FirstGroupNode"/>
</node>
<node ID="ID_489506209" CREATED="1742386650812" MODIFIED="1742388611973"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      build_matrix()
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="contigs" VALUE=""/>
<attribute NAME="contigs_size" VALUE=""/>
<attribute NAME="pairs_files" VALUE=""/>
</node>
<node TEXT="" ID="ID_15307892" CREATED="1742388205005" MODIFIED="1742388205008">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node ID="ID_795860118" CREATED="1742388205012" MODIFIED="1742394825343"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      output : <font color="#006666">mat</font>
    </p>
  </body>
</html>

</richcontent>
<arrowlink SHAPE="CUBIC_CURVE" COLOR="#000000" WIDTH="2" TRANSPARENCY="200" DASH="3 3" FONT_SIZE="9" FONT_FAMILY="SansSerif" DESTINATION="ID_1224680280" STARTINCLINATION="-48;69;" ENDINCLINATION="78;11;" STARTARROW="NONE" ENDARROW="DEFAULT"/>
</node>
</node>
</node>
<node TEXT="" POSITION="right" ID="ID_157473920" CREATED="1742388358538" MODIFIED="1742388358543">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Outputs" ID="ID_209642331" CREATED="1742388358546" MODIFIED="1742395353196">
<node TEXT="mges_data" ID="ID_998214364" CREATED="1742395317946" MODIFIED="1742395360739"/>
<node TEXT="mge_bins" ID="ID_31862007" CREATED="1742395329163" MODIFIED="1742395340764"/>
</node>
</node>
<node TEXT="" POSITION="right" ID="ID_393358706" CREATED="1742389579753" MODIFIED="1742389579754">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_611406252" CREATED="1742386182857" MODIFIED="1742389546821"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      generate_bin_summary()
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="contigs_data" VALUE=""/>
<attribute NAME="mge_bins" VALUE=""/>
<attribute NAME="outfile" VALUE=""/>
</node>
<node TEXT="" POSITION="right" ID="ID_1304223272" CREATED="1742389579742" MODIFIED="1742389579752">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Output : summary (csv)" ID="ID_1778573253" CREATED="1742389579755" MODIFIED="1742389601687"/>
</node>
<node TEXT="" POSITION="right" ID="ID_702687538" CREATED="1742389366815" MODIFIED="1742389366818">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="right" ID="ID_1167321395" CREATED="1742386243361" MODIFIED="1742389358509"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u><b>Function</b></u></i>
    </p>
    <p>
      build_mge_depth()
    </p>
  </body>
</html>

</richcontent>
<attribute_layout NAME_WIDTH="71.99999785423284 pt"/>
<attribute NAME="contigs_file" VALUE=""/>
<attribute NAME="depth_file" VALUE=""/>
<attribute NAME="mges_data" VALUE=""/>
<attribute NAME="mges_depth_file" VALUE=""/>
</node>
<node TEXT="" POSITION="right" ID="ID_349525600" CREATED="1742389366809" MODIFIED="1742389366815">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Output: mge_depth (csv)" ID="ID_457253277" CREATED="1742389366819" MODIFIED="1742389605347"/>
</node>
<node TEXT="" POSITION="left" ID="ID_1899182547" CREATED="1742390720369" MODIFIED="1742390720371">
<hook NAME="FirstGroupNode"/>
</node>
<node POSITION="left" ID="ID_129136412" CREATED="1742386402986" MODIFIED="1742390666774"><richcontent TYPE="NODE">

<html>
  <head>
    
  </head>
  <body>
    <p>
      <i><u>Function</u></i>
    </p>
    <p>
      generate_mges_fasta()
    </p>
  </body>
</html>

</richcontent>
<attribute NAME="fasta" VALUE=""/>
<attribute NAME="mge_bins" VALUE=""/>
<attribute NAME="outfile" VALUE=""/>
<attribute NAME="tmp_dir" VALUE=""/>
</node>
<node TEXT="" POSITION="left" ID="ID_134690029" CREATED="1742390720366" MODIFIED="1742390720367">
<hook NAME="SummaryNode"/>
<hook NAME="AlwaysUnfoldedNode"/>
<node TEXT="Output : outfile that contains&#xa;all bin&apos;s fasta files produced by checkv" ID="ID_241471540" CREATED="1742390720372" MODIFIED="1742395902900"/>
</node>
<node TEXT="Outputs" POSITION="left" ID="ID_1943541674" CREATED="1742396112066" MODIFIED="1742396137779">
<node TEXT="" ID="ID_1179681442" CREATED="1742396126471" MODIFIED="1742396126471"/>
<node TEXT="" ID="ID_1049766896" CREATED="1742396173877" MODIFIED="1742396173877"/>
<node TEXT="" ID="ID_1101518447" CREATED="1742396189614" MODIFIED="1742396189614"/>
<node TEXT="" ID="ID_1889427896" CREATED="1742396210188" MODIFIED="1742396210188"/>
</node>
<node TEXT="" POSITION="left" ID="ID_1795825589" CREATED="1742396987201" MODIFIED="1742396987201"/>
</node>
</map>
