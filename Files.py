#Files.py
#Contains functions dealing with opening, and writing files

import os

def DesktopPath(file):
    root = "/Users/coreygardner/Desktop/"
    return os.path.join(root,file)
""" takes:File name saved on desktop
    Returns:Path to file on Desktop
"""

def DesktopCreate(file):
    root = "/Users/coreygardner/Desktop/"
    file = os.path.join(root,file)
"""Takes:name of file you want to create
    Returns:Path name of file you will create, and opened file"""

def FileReader(file):
    file = open(file,"r")
    return file.read()
"""Takes:Path of file to be read
    Returns:readable version of file
"""

def FileReadLines(file):
    file = open(file, "r")
    file = file.readlines()
    return file
""""Takes: File Path
    Returns: list of lines in file
"""


def ListStrip(listset):

    blank_list = []
    for i in range(len(listset)):
        current = listset[i]
        blank_list.append(current.replace(" ",""))
    return blank_list
"""Takes: a list of strings
    Returns: a list of strings w/o spaces
"""

def ListWriter(listset,file):
    base = "Users/coreygardner/Desktop/"
    file = os.path.join(base,file)
    file = open(file,"w")
    for i in range(len(listset)):
        file.write(listset[i])
    file.close()
    return file
"""Takes: List, Pathname of file to be wrote
    Returns: written file with contents of list
"""


file = DesktopPath("arabstrip.txt")
read = FileReadLines(file)
list = ListStrip(read)
new_file = open("Users/coreygardner/Desktop/HOG.txt","w")
for i in range(len(list)):
    new_file.write(list[i])
new_file.close()