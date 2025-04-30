### Author:  Samantha Scibelli
### Date:    April 18th, 2025
### Updated: April 29th, 2025
### Purpose: Automate process of taking raw otf maps from .smt files to CLASS files

import os 

#User inputs file number
n = input("File Number: ")

#User inputs scan numbers
startscan = input("Start Scan: ")
endscan   = input("End Scan:   ")

#User inputs for backend
telescope = input("Telescope backend name (fqm/f1m/sww): ")
sb = input("Telescope sideband (u/l): ")

#Options for non-user inputs:
init = 'cjl'
#sb = 'l'

if telescope == 'sww':
    startname = 'sww'
else:
    startname = 'ffb'


#Run the command for both polarizations
#os.system(
print('otf2class -bs '+str(startscan)+' -es '+str(endscan)+' -s 2 -i '+str(telescope)+'-h'+str(sb)+' -o . sdd_'+str(startname)+'.'+str(init)+'_'+str(n).zfill(3))
os.system('otf2class -bs '+str(startscan)+' -es '+str(endscan)+' -s 2 -i '+str(telescope)+'-h'+str(sb)+' -o . sdd_'+str(startname)+'.'+str(init)+'_'+str(n).zfill(3))
os.system('otf2class -bs '+str(startscan)+' -es '+str(endscan)+' -s 2 -i '+str(telescope)+'-v'+str(sb)+' -o . sdd_'+str(startname)+'.'+str(init)+'_'+str(n).zfill(3))

