import re
vs = open("/Users/coreygardner/Desktop/ContigV2.txt", "r")
search = vs.read()
# Opens up vector sequence in string format
vector_regex = re.compile(search, re.DOTALL) # Str of Vector sequence passed to regex search
sequence = open("/Users/coreygardner/Desktop/Contig.txt", "r")
strsequence = sequence.read()
new_Sequence = vector_regex.sub(" ",strsequence )
new_file = open("/Users/coreygardner/Desktop/ContigFinal", "w")
new_file.write(new_Sequence)



#Open up Vector file
#read in string format
#pass the string into a regex search
#Open up file containing the sequences, read the file
#Using Regex search strip File of Vector
#Write this sequence to a new file