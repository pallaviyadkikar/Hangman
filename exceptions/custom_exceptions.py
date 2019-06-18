'LeaderBoard'
class EmptyCategoryList(Exception):
    def __init__(self):
        print("#############******Uh! No Player Found**************##################");
    
'Admin'
class InvalidPassword(Exception):
    def __init__(self):
        print("#############*********Invalid Password*********###########");
class PasswordMismatch(Exception):
    def __init__(self):
        print("##############*********Password Mismatch*********##############");
'Add/Edit'
class QuestionId(Exception):
    def __init__(self):
        print("##############********* Question Id Mismatch*********##############");
class Cateogry(Exception):
    def __init__(self):
        print("##############********* Category Mismatch*********##############");
'Delete'    
class QuestionInvalid(Exception):
    def __init__(self):
        print("##############********* Question Invalid*********##############"); 
class QuestionIDInvalid(Exception):
    def __init__(self):
        print("##############********* QuestionID mismatch *******##############"); 
'Play'
class NameException(Exception):
    def __init__(self):
        print("##############********* Name exists already*********##############");  
class NoCategory(Exception):
    def __init__(self):
        print("##############********* No Category given*********##############");
class QuestionsDone(Exception):
    def __init__(self):
        print("##############********* Kindly add more questions to continue more level*********##############");
class Invalid(Exception):
    def __init__(self):
        print("##############********* Invalid Option*********##############"); 
        
class GameOver(Exception):
    def __init__(self):
        print("#############********GAME OVER**********############");
class Exit(Exception):
    def __init__(self):
        pass

    
    