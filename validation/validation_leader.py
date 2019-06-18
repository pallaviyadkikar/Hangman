
from database import db_leader

def validate_category(cat):
    catte=cat.lower();
    if(catte in ['movies','country']):
        return True
    else:
        #print("*******No Player Found*********")
        return False
        
def validate_city(city):
    if(city in db_leader.get_city()):
        return True
    else:
        #print("*********Invalid City**********")
        return False

def validate_name(name):
    if(name in db_leader.get_name()):
        return True
    else:
        #print("***************No Player Found*****************")
        return False
def validity_yesno(x):
    if (x=='Y' or x=='y'):
        return True
    else:
        #print("*********Invalid Checking**********")
        return False
    
def validate_selection(player):
    if(int(player)>=3 and int(player)<=10):
        return True
    else:
        #print("********* Invalid Selection **********")
        return False
    