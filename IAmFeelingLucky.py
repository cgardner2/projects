#! usrs/bin/env python3
#IAmFeelingLucky Google  Search
#Searchs in the browser and will open the links to all of the search results on the first page

#Step 1: Get command line arguments and Request the search page

import requests,sys,webbrowser , bs4
print("Googling...")

#Gets search topic from the command line
res = requests.get("http://google.com/search?q=" + ''.join(sys.argv[1:]))

try:
    res.raise_for_status()
except Exception as err:
    print("There was a problem: %s" %err)

#retrieves top search results
soup = bs4.BeautifulSoup(res.text) # Turns the link into a text format, which makes it readable for bs4

#Opens a browser tab for each result
LinkElems = soup.select(".r a") # Creates a list of all of the a elements that are within the class r
numOpen = min(5, len(LinkElems)) #Opens five or length of the LinkElems list
for i in range(numOpen):
    webbrowser.open("http://google.com" + LinkElems[i].get('href'))
    # For each list item in LinkElems opens up a new page
    #href uses.get on the href attribute to return the string of the website adress stored within it

