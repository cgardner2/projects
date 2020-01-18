#! /usr/bin/env Python 3
# Renames files with American date Format to European date format
import shutil,os, re

#Create a regex to match files with the American date format
# whyd he use 3 string
datepattrn = re.compile(r'''^(.*?) # All text before the date
((0|1)?/d)- # One or Two digits for the month
((0|1|2|3)?/d)- # one or two digits for the day
((19|20)/d/d) # four digits for the year
(.*?)$ # matches text after the date
''', re.VERBOSE
)

#Loop over filess in the WD
for amerFilename in os.listdir('.'):
    mo = datepattrn.search(amerFilename)

    #Skip Files w/o a date
    if mo == None:
        continue

    #Get the different parts of a files name
    beforepart = mo.group(1)
    monthpart = mo.group(2)
    daypart = mo.group(4) # groups are number by the first ( opening parenthesis
    yearpart = mo.group(6) # Just count the open parenthesis to understand the grouping
    afterpart = mo.group(8)

# Forms the European Style File Name !! Should everything following this line of code still be in the for loop?? yes probably
    euroFilename = beforepart + daypart + "-" + monthpart + "-" + yearpart + afterpart

# Get the full absolute file paths
    absworkingdir = os.path.abspath(".") #what does the little . do i think it refers to the entire parent folder
    amerFilename = os.path.join(absworkingdir, amerFilename)
    euroFilename = os.path.join(absworkingdir, euroFilename)

#rename the files
print("renaming "%s" to "%s" ... "% (amerFilename, euroFilename))  #<<<<<- tf does this mean
#shutil.move(amerFilename, euroFilename) # uncomment after testing





# project -> create a program to go through all your old school junk files and delete them .docx and (d/) for opening random downloads from school multiple times