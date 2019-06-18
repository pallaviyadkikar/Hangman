'''
Created on Feb 16, 2017

@author: jeevan.kj
'''
'LeaderBoard'
class EmptyCategoryList(Exception):
    def __init__(self):
        print("#############******Uh! No Player Found**************##################");

class InvalidSel(Exception):
    def __init__(self):
        print("#############******selection should be take between the limit**************##################");

class InvalidChecking(Exception):
    def __init__(self):
        print("#############******should take valid selection from (Y/N)**************##################");

class InvalidCity(Exception):
    def __init__(self):
        print("#############******Not valid city**************##################");