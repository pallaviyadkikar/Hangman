from database import DB_play
from utility import ShowGraphics
def check_unique_name(name):
    if(DB_play.check_names(name)):
        return False
    return True



def show_hangman(no_of_failed_attempt):
    if(no_of_failed_attempt==0):
        ShowGraphics.show_hang_man(0)
    elif(no_of_failed_attempt==1):
        ShowGraphics.show_hang_man(1)
    elif(no_of_failed_attempt==2):
        ShowGraphics.show_hang_man(2)
    elif(no_of_failed_attempt==3):
        ShowGraphics.show_hang_man(3)
    elif(no_of_failed_attempt==4):
        ShowGraphics.show_hang_man(4)
    elif(no_of_failed_attempt==5):
        ShowGraphics.show_hang_man(5)
    elif(no_of_failed_attempt==6):
        ShowGraphics.show_hang_man(6)
        