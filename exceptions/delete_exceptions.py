'''
Created on Feb 16, 2017

@author: jilu.james01
'''

class CategoryInvalid(Exception):
    def __init__(self):
        print("##############********* Category Mismatch*********##############");

class QuestionIDInvalid(Exception):
    def __init__(self):
        print("##############********* QuestionID mismatch *******##############"); 
        
class NoLevel(Exception):
    def __init__(self):
        print("##############********* No level exist *******##############"); 

class Invalid(Exception):
    def __init__(self):
        print("##############********* Invalid Option*********##############"); 
        
