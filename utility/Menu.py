
from functionality.leader import leader_board
from functionality.admin_function import admin
from functionality.play_module import play_main
'''
This module displays a menu to the user.
'''
print("+------------------------+")
print("| Ready to Play PyAngMan |")
print("+------------------------+")

print("Choose an option from below:\n")

end=False

while(end==False):
    try:    
        print("1. Play")
        print("2. Leader Board")
        print("3. Admin Menu")
        print("4. Quit")
        option=input()
        if(option.isdigit() and (int(option)>=1 or int(option)<=4)):
            if(int(option)==1):
                print("Play PyAngMan:")
                play_main();
               
            if(int(option)==2):
                print("PyAngMan Leader Board:")
                leader_board();
                
            if(int(option)==3):
                print("PyAngMan Admin Menu:")
                admin();
                
            if(int(option)==4):
                print("Thank you!")
                end=True
        else:
            print("Please enter a valid option ( 1,2,3,4)")
    except Exception as e:
        print(e)
        
        