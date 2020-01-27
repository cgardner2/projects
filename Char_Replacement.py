#Char_replacemnt will find substitutions and edit the file with the proper character
# ex: degrees -> ° or microliters -> μl

file_path = open("/Users/name/domain/file_name.txt", "r")
file = file_path.readlines()
new_file = open("/Users/name/domain/new_file.txt", "w")
for line in file:
    new = line.replace("degrees", "°")
    new_file.write(new)

