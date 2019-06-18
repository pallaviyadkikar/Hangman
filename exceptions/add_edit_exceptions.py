class Category(Exception):
    def __init__(self):
        print("##############********* Category Mismatch*********##############");

class QuestionID(Exception):
    def __init__(self):
        print("##############********* QuestionID mismatch *******##############"); 
        
class LevelInvalid(Exception):
    def __init__(self):
        print("##############********* Level Mismatch *******##############"); 

class Invalid(Exception):
    def __init__(self):
        print("##############********* Invalid Option*********##############"); 
        