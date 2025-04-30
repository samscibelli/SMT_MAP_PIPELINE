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

***6) Scale the Data***

Similar to the above flow, next, run the 06_scaleall.class file on the .base files you just created. 
Again, keep track of the files you create!

Run the script within CLASS, 

>> LAS > @06_scaleall.class

The script will ask you: 

1) What data file you want to baseline (e.g., class_f1m_hl_ces_012.base)

2) What the name of your output file will be (e.g., class_f1m_hl_ces_012)
The script will automatically give the extension as ‘.scale

3) What factor to multiply your data - this factor is based on the main beam temperature efficiencies (e.g., if your efficiency is 70% you multiple by 1.43). ARO compiles these efficiencies into spreadsheets, which you can find here(https://aro.as.arizona.edu/?q=beam-efficiencies)

4) Whether you are writing a new file or not 

NOTE: If you are just reducing single-pointing data, you can skip ahead to combining and summing! :) 

***7) Convolve the Data***

Similar to the above flow, next, run the 07_convolve.class file on the new .scale files you just created. 

Again, keep track of the files you create! 

Before diving in, you’ll need to know in arcseconds the size of the data cube and pixel spacing! See Mangum et al., 2007 "A suitable cell size would be less than or equal to 1/3 of the single-dish-beam-size”

Run the script within CLASS, 

>> LAS > @07_convolve.class

The script will ask you: 

1) What data file you want to baseline (e.g., class_f1m_hl_ces_012.scale)

2) What the name of your output file will be (e.g., class_f1m_hl_ces_012)
      a) The script will automatically give the extension as ‘.conv

3) Information about the convolving: 
      a) The minimum RA offset (in units of arcseconds)
   
      b) The maximum RA offset (in units of arcseconds)
   
      c) The minimum DEC offset (in units of arcseconds)
   
      d) The maximum DEC offset (in units of arcseconds)
   
          - E.g., if your map is 5x5 arcmin, then from the center your minimum values are -150 arcseconds and maximum values are 150 arcseconds
      e) Enter the Step Size (in units of arcseconds)

           - 1/3 of the beam size or smaller
   
      f) Enter the FWHM of New Beam (in units of arcseconds)
   
      g) Enter the FWHM of Old Beam (in units of arcseconds)
   
          - Old beam must be smaller!

4) Whether you are writing a new file or not 

*You can also edit the script to hard-wire the convolving information if you have many maps to run through with the same mapping info from point 3) above!

***8) Combine the Data***

To combine the data, you will first need to copy over the first file into a file you would like to combine all the scans into, i.e., 

>> cp class_f1m_hl_ces_012.conv class_f1m_hl_ces.comb

Then, keep track of the amount of observation numbers for each map, as you will need to give the new starting number each time you add a map to this combined file. 

Then, you can run the 08_combine.class file in CLASS: 

<< LAS > @08_combine.class

The script will ask you: 

1) What data file you want to add to the combined file

2) What the name of your output file is that you just created (e.g., class_f1m_hl_ces.comb)

3) What the scan number is to start this new set of map scans 

***9) Sum the Data***

	Typically to save on data space, each position in the map can be ‘summed’ together. Unfortunately it is currently not available. This shouldn’t affect the resulting maps!
 
***10) Fit the Data and Make the Map!***

Run the 10_map_fitting.pro class file in CLASS: 

>> LAS > @10_map_fitting.pro 

The script will ask you: 
What data file you want to fit 
What the new names of the files should be 





