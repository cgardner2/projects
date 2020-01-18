#! /usr/bin/env Python 3
import re, os ,shutil, send2trash, logging

# Step 1 creating a regex search to match the names of files that have been dowloaded more then once
file_pattern = re.compile("""
(\.*) # back slash used to indicate you want to match anything

(\(\d\)) # Ex. would match (1) indicating the file has been downloaded more then once

(.pptx|.docx|.jvl|.ppt|.doc) #pipe to match the match the various file extensions

""", re.VERBOSE)

#Step 2 create a folder to store the junk in, then move this folder to the trash
newpath = r'/Users/coreygardner/Desktop/junkfolder'
if not os.path.exists(newpath):# Checks to see if the path exist, if it doesn't the new path is created
    os.makedirs(newpath)

#Step 3: Walk the downloads folder and search the files

downloads_folder = "/Users/coreygardner/Downloads" #creates variable storing download folder name


for folderName, subfolders, filename in downloads_folder:
    mo = file_pattern.search(filename)
    if mo == None:
        continue  # If search does not return anything then the program will just continue
    else:
        shutil.move(filename, newpath) # will this take into account the filename without the entire path or will it automatically put the path in filename


for folderName, subfolders, filename in newpath:
    send2trash.send2trash(newpath)
else:
    print("Have a good day")