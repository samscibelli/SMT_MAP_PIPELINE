DEFINE CHARACTER FILEIN*40 FILEOUT*40 FILEIN2*40

SAY "ENTER INPUT FILE NAME: "
LET FILEIN = &1
FILE IN 'FILEIN'
FIND
LIST

set unit v
set mode x auto

find
list
set nomatch

set win 0 10

SET EXTENSION .BIN
SAY "ENTER OUTPUT FILE NAME (.bin extension): "
LET FILEOUT = &2

file out 'FILEOUT'  single /overwrite

for ientry 1 to found 
get n 
lines 1 "0 1 0 4 0 1" /nocursor
base
min
!smooth hanning 2
write
next

!not necessary 
!SET EXTENSION .out
!SAY "ENTER OUTPUT .out:"
!LET FILEIN2 = &3
!FIND
!LIST
!print fit /output 'FILEOUT'

!! CREATE THE MAP 
SAY "ENTER table/map NAME: "
LET FILEIN2 = &3
FILE IN 'FILEIN2'
FIND
LIST


file in 'FILEOUT'
set weight equal
find
set nomatch

table 'FILEIN2' new
let MAP%TOLE = 1
xy_map 'FILEIN2'  /nogrid 

