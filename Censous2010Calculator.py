
#ReadCensusExcel.py
#Tabulates number of censous tracts and population for each county
import openpyxl,pprint
wb = openpyxl.load_workbook("/Users/coreygardner/Desktop/censuspopdata.xlsx")
sheet = wb.get_sheet_by_name("Population by Census Tract")
countyData ={

}

# To do Fill in County Data with Censous tract and Population
for row in range(2, sheet.max_row +1):
    # Each row in spreadsheet has data for one censous tract
    state = sheet["B" + str(row)].value
    county = sheet["C" + str(row)].value
    pop =  sheet["D" + str(row)].value

#Makes sure the Key for the State exist
    countyData.setdefault(state, {})
#makes sure the county exist as a key for the state
    countyData[state].setdefault(county, {"tracts":0 , "pop":0})
#each row represents one censous tract so increment by 1
    countyData[state][county]["tracts"] +=1
#Increase county pop by pop in censous tract
    countyData[state][county]["pop"] += int(pop)

#Writes a file of the calculations
result = open("/Users/coreygardner/Desktop/census2010.py", "w")
result.write("all data = " + pprint.pformat(countyData))
result.close()