class InvalidEmptyString(Exception): 
    def __init__(self):
        super().__init__("** ID CANNOT BE EMPTY")

class InvalidID(Exception):
    def __init__(self):
        super().__init__("QuestionId is invalid.Please check the QuestionId")

class InvalidLevel(Exception):
    def __init__(self):
        super().__init__("** NO QUESTIONS FOUND FOR ABOVE CRITERIA")   

class InvalidCategory(Exception):
    def __init__(self):
        super().__init__("** NO QUESTIONS FOUND FOR ABOVE CRITERIA")  
        
class InvalidQuestionSubString(Exception):
    def __init__(self):
        super().__init__("There is no match found.Try another question.")
        
class Put_Correct_Input1(Exception):
    pass


class Finish(Exception):
    pass
class Exit_Play(Exception):
    pass
class input_play_login(Exception):
    pass
class invalid_name(Exception):
    pass
class invalid_integer(Exception):
    pass
class no_more_ques(Exception):
    pass
class invalid_category(Exception):
    pass
class quitt(Exception):
    pass
class Give_correct_input(Exception):
    pass
class Unique_violation(Exception):
    pass
class edit_start_again(Exception):
    pass


'''
here all the exceptions needed for the project are specified clearly
'''
class InvalidCategoryException(Exception):
    def __init__(self,category):
        super().__init__(" *** CATEGORY "+ category +" NOT FOUND")


class WrongPassword(Exception):
    pass
class WrongConfirmPassword(Exception):
    pass
class InvalidCommand(Exception):
    pass

