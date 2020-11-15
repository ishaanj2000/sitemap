#importing libraries
import re, requests
import xml.etree.ElementTree as tree
from bs4 import BeautifulSoup as bs

# to check if the ur input is valid using regex
def isValid(string):
    exp = ("((http|https)://)(www.)?" +
             "[a-z]+"+ "." + "[a-z]+$")    
    
    if(string == None):
        print("No url")
    
    if(re.search(exp, string)):
        return True
    else:
        return False 
        
input_url = str(input())
if (isValid ==True):
    
#use bs4 to read the content of the page
    source_page = requests.get(input_url)
    sitemap = bs(source_page.content, 'html.parser')
#append the required data to a list called urls
    urls = [ele.text for ele in sitemap.findAll('loc')]
    
    
#write the data of the list to an xml file  
    xml_output_file = open("sitemap.xml", w+) 
    for url in urls:
    xml_output_file.write(url)
    







