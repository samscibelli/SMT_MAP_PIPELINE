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

>> ssh -Y obs@smtoast.as.arizona.edu	(enter password)

Next, type in observers initials 
Now you are in the directory to run the mapping pipeline!

NOTE: you need to make sure your computer's IP address can log into the arizona computer 

2) Collect Map Scan Numbers:

Record the beginning and ending scan numbers for each map in the raw data files (.smt files)
Each map should have the same number of scans (a 5’x5’ map has 45 scan

3) Run Python Script for OTF to CLASS

Run in the terminal python script provided, 

>> python 01_script_otf_to_class.py 

The script has hard-wired the observer initials, so change if needed. 

You’ll need to know, 
Data file the mapping data comes from
Beginning scan number 
End scan number
The backend name 
Telescope sideband (upper or lower)

The script will produce the CLASS map files that start with ‘class.sdd’ in the name for both vertical and horizontal polarizations. 

NOTE: If you have individual maps in the same data file you can either ‘append’ to the same ‘class.sdd’ file or re-name files to indicate a new map has been produced by the same data file 



