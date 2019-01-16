class InvalidCategoryException(Exception):
    def __init__(self):
        super().__init__("This category is invalid")
        
class InvalidLevelException(Exception):
    def __init__(self):
        super().__init__("This level is invalid")
     
class InvalidChoiceSelection(Exception):
    def __init__(self):
        super().__init__("This Choice is invalid")

class InvalidOptionSelection(Exception):
    def __init__(self):
        super().__init__("This Option is invalid")

class InvalidCommandException(Exception):
    def __init__(self):
        super().__init__("**INVALID COMMAND")

class InvalidPasswordException(Exception):
    def __init__(self):
        super().__init__("**INVALID PASSWORD")

class LoginUnsuccessfulException(Exception):
    def __init__(self):
        super().__init__("Login Unsuccessful")
        
        
class NoDataException(Exception):
    def __init__(self):
        super().__init__("No data available")






class NoIdFound(Exception): 
    def __init__(self):
        super().__init__("No id")


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