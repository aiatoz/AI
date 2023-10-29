# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:52:01 2023

@author: Krishna
"""


from selenium import webdriver
import time


'''Driver will open up instagram, Sign in manually, go to post, then come back, type ready. Then it will fetch the comments and
mark spam'''


driver = webdriver.Chrome()

print("Sign in to Instagram, goto any posts and type ready") 

instURL=input("Enter the URL :")
driver.get(instURL)