#Opens all .txt files , and searches for regex expression , prints results


#Go to folder, and loop through all of the files that end in a txt extnsion
file = open("/Users/coreygardner/Desktop/Txt practice folder")
for document in file:
    if document.endswith(".txt"):
        open(document)


#create a regex search to look for patterns in a document

# print whcih files cntn the expression