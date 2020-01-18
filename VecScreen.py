import pyperclip
file = open("/Users/coreygardner/Desktop/Contig.txt", "r")
filestr = file.read()
from selenium import webdriver as wd
driver = wd.Firefox(executable_path="/Users/coreygardner/geckodriver")
driver.get("https://www.ncbi.nlm.nih.gov/tools/vecscreen/")
Queryelem = driver.find_element_by_id("QUERY")
Queryelem.click()
Queryelem.send_keys(filestr)
button_elem = driver.find_element_by_id("vecsreen-submit")
button_elem.click()
Vec_elem = driver.find_element_by_class_name("button")
Vec_elem.click()
driver.implicitly_wait(5) #waits 5 seconds