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

***1) Logging Into Arizona Computer:***

>> ssh -Y obs@smtoast.as.arizona.edu	(enter password)

Next, type in observers initials 
Now you are in the directory to run the mapping pipeline!

NOTE: you need to make sure your computer's IP address can log into the arizona computer 

***2) Collect Map Scan Numbers:***

Record the beginning and ending scan numbers for each map in the raw data files (.smt files)
Each map should have the same number of scans (a 5’x5’ map has 45 scan

***3) Run Python Script for OTF to CLASS***

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

NOTE: If you have individual maps in the same data file you can either ‘append’ to the same ‘class.sdd’ file or re-name files to indicate a new map has been produced by the same data file (I recommend the latter).  

***4) Inspect the data in CLASS (optional)***

The spectra can be averaged together and inspected in the CLASS program at this point:

In the terminal type, 

>> CLASS 

Now, within CLASS, 

>> LAS> file in “filename”	! reads the datafile
>> LAS> dev i w			! opens the graphics window 
>> LAS> find				! populates the list with observations
>> LAS> set nomatch			! ignores the offset in position when averaging 
>> LAS> av /r				! averages the list population 
>> LAS> plot				! plot the spectrum

***5) Baseline the Data***

First, run the 05_baseline.class file on all of the data files you created. 
Before you do,

1) You will need to keep track of the input and output file names either in a spreadsheet or text file! 
2) *In the script, a window around the line of interest is hard-wired. Adjust this as needed.

After these initial steps, run the script within CLASS, 

>> LAS > @05_baseline.class

The script will ask you: 
1) What data file you want to baseline (e.g., class.sdd_f1m-hl.ces_012)

2) What the name of your output file will be (e.g., class_f1m_hl_ces_012)
The script will automatically give the extension as ‘.base’

3) What baseline order is needed 

4) Whether you are writing a new file or not 

Note: the current script doesn’t smooth the data, but it is possible to change this

*Run the script for all the files!*


