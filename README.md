**SMT Mapping Pipeline**

This pipeline assumes you have all necessary scripts in your directory: 

01_script_otf_to_class.py

05_baseline.class

06_scaleall.class

07_convolve.class

08_combine.class

09_sumall.class

10_map_fitting.pro 

bigbeam.class

1) Logging Into Arizona Computer: 

>> ssh -Y obs@smtoast.as.arizona.edu	(pw: 10MAstronomyFactory)

Next, type in observers initials 
Now you are in the directory to run the mapping pipeline!

NOTE: you need to make sure your computer's IP address can log into the arizona computer 

2) Collect Map Scan Numbers:

Record the beginning and ending scan numbers for each map in the raw data files (.smt files)
Each map should have the same number of scans (a 5’x5’ map has 45 scan
