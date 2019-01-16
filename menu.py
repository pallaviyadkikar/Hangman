fromom functionality.Admin_add_edit_menu import admin
from utility import connection
from functionality import leaderboard
from functionality import play

con=connection.create_connection()
cur=connection.create_cursor(con)
cur1=connection.create_cursor(con)
'''
This module displays a menu to the user.
'''

print("+-------------------------+")
print("| Ready to Play PyAngMan |")
print("+------------------------+")

print("Choose an option from below:\n")

end=False

while(end==False):
    print("1. Play")
    print("2. Leader Board")
    print("3. Admin Menu")
    print("4. Quit")
    option=input()
    if(option.isdigit() and (int(option)>=1 and int(option)<=4)):
        if(int(option)==1):
            print("Play PyAngMan:")
            p=play.play()
            p.play_login(cur,con)
        if(int(option)==2):
            print("PyAngMan Leader Board:")
            l=leaderboard.leaderboard()
            l.leader(con,cur)
        if(int(option)==3):
            print("PyAngMan Admin Menu:")
            admin(cur,cur1,con)          
        
           
        if(int(option)==4):
        
            print("Thank you!")
            end=True
    else:
        print("Please enter a valid option ( 1,2,3,4)")

cur.close()
cur1.close()
con.close()
   