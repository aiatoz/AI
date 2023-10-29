# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 11:59:42 2023

@author: Krishna

Useful URLs:
    
https://www.selenium.dev/documentation/webdriver/elements/locators/
https://pypi.org/project/selenium/
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import locate_with
import time
import re
import csv
import os


def getTextFromAnchor(content): #To separate anchor content
    cleanAnchor = map(''.join, re.findall(r'<a\s[^>]*>([^<]*)</a>|\b(\w+://[^<>\'"\t\r\n\xc2\xa0]*[^<>\'"\t\r\n\xc2\xa0 .,()])', content))
    return list(cleanAnchor)



def cleanHashTags(content): #Replaces all anchors with mentioned IDs
    #cleanAnchor will have the mentioned ID text 
    cleanAnchor = getTextFromAnchor(content)
    for i in cleanAnchor:
        leftOut = content.split(i)              #Splits using each of the ids
        woAnchor = leftOut[0].split('<a ')[0]   #Leaves the anchor tag and takes it's left part
        
        content = woAnchor+i+leftOut[1][4:]    #Combines the left + mentioned_id + right

    return content
    


driver = webdriver.Chrome()


'''
https://www.instagram.com/p/CwrqsNCOlin/
https://www.instagram.com/p/Cy8fljmRr3l/
https://www.instagram.com/p/Cy71iUHRNmF/
https://www.instagram.com/p/Cy6s8y4qlSS/
https://www.instagram.com/p/ClKYC31vvhS/
'''

instURL="https://www.instagram.com/p/Cy7vD6ttgn7/?hl=en"
driver.get(instURL)


driver.implicitly_wait(30)
elements = driver.find_elements(By.CLASS_NAME,"_aade")

instaData = []

for e in elements[2:-1]:#Trim down the post content and leave the comments. If you need to see, try removing the slice
    content = e.get_attribute('innerHTML')
    
    #-------------Get IDs----------------#
    idElement = driver.find_element(locate_with(By.CLASS_NAME, "_a9zc").near(e))
    idContent = idElement.get_attribute('innerHTML')
    
    print(getTextFromAnchor(idContent)[0])
    instaID = getTextFromAnchor(idContent)[0]
    
    
    #-------------Get Comments--------------#
    if '<a' in content:
        content = cleanHashTags(content)
        
    print(content)
    instaComment = content
    
    
    #------------Preparing data-------------#
    instaData.append(['--',instaComment,instaID])
    




#Setting file for wriiting down InstaComments
fields = ['Label','Comments','ID']

# Write the data to the CSV file
with open('instaComments.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
    for row in instaData:
        writer.writerow(row)
    
    #print(content.strip())
    #f.write(content.strip()+'\n')
#f.close()