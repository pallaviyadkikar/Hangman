
from exceptions import exceptions
from functionality import edit
from functionality import deletemod
import re
from functionality import add
from functionality import AdminAccess
def admin(cur,cur1,con):
    
    end=False
    
    admin=AdminAccess.AdminAccess()  
    
    admin.admin_menu(cur,con)
    
    while(end==False):
        print("\n=================================")
        print("What would you like to do ?")
        print("=================================")
        print("Password")
        print("Add")
        print("Edit")
        print("Delete")
        print("Logout")
        print("Quit")
        try:
            option1=input()
            option=option1.lower()
            if(not option.isdigit()):
                if(str(option)=="add"):
                    #show_Recent_que_added()
                    
                    print("PyAngMan Add Question:")
                    o=add.add()
                    o.add_question(cur,con)
                    
                   
                elif(str(option)=="edit"):
                    print("PyAngMan Leader Board:")
                    e=edit.edit()
                    e.show_rec_edited(cur,cur1,con)
    
                
                elif option=='password':
                    admin.change_password(cur,con)
                
                elif option=='logout':
                    admin.logout(cur,con)
                    admin.admin_menu(cur,con)
             
              
                elif(str(option)=="quit"):
                    print("Thank you!")
                    end=True
                
                
                elif(re.search(r"edit\s\d{3}",str(option))!=None):
                    qid=int(option[5:])
                    m=edit.edit()
                    cur.execute("select qid ,category,qname, lvl from questions where qid ='"+str(qid)+"'")
                    m.quick_update(cur,cur1,con, qid)
                    
                elif(option.lower()=="delete"):
                    d=deletemod.delete()
                    d.delete(cur,con,cur1,option.lower())
                    
                elif(re.search(r"delete\s\d{3}",str(option.lower()))!=None):
                    d=deletemod.delete()
                    d.delete(cur,con,cur1,option.lower())
                    
                else:
                    raise exceptions.InvalidCommandException
            else:
                raise exceptions.InvalidCommandException
        except exceptions.InvalidCommandException as e:
            print(e)