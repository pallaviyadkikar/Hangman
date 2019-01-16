
from exceptions import exceptions



class edit:
    
    def show_rec_edited(self,cur,cur1,con):
        cur.execute("select * from edited_q")
        data=cur.fetchone()
    
        if data is None:
            print("No recently edited questions")
            self.get_values(cur,cur1,con)
        else:
            count=0
            cur.execute("select qid,qname,lvl from edited_q order by edited_time desc")
            print("Recently edited Questions:")
            print("=============================")
            for qid,qname,lvl in cur:
                print(str(qid)+"\t"+qname+"\t"+lvl)
                count+=1
                if count==5:
                    break
                
            self.get_values(cur,cur1,con)
          
                
                
        con.commit()
    def get_values(self,cur,cur1,con):
       
        print("PyAngMan Edit Question:")
        print("")
        print("Enter Question Number/Category/ALL/QUIT:")
        try:    
            choice=input()
            if str(choice)=="Country" or str(choice)=="Movie":
                self.display_catagorywise(choice,cur,cur1,con)
               
            elif str(choice)=="All":
                self.display_all(cur,cur1,con)
                
            elif choice=="Quit":
                flag=True
            
            elif choice=="Number":
                self.display_all(cur,cur1,con) 
            else:
                raise exceptions.InvalidOptionSelection   
            con.commit()
        except exceptions.InvalidOptionSelection as e:
            print (e)
        
    def display_catagorywise(self,choice,cur,cur1,con): 
        cur.execute("select qid,qname,lvl from questions where category='"+choice+"'")
        
        for qid,qname,lvl in cur:
            print(str(qid)+"\t"+qname+"\t"+lvl)
        self.edit_question(cur,cur1,con)
         
        con.commit()      
    def display_all(self,cur,cur1,con):
        cur.execute("select qid,qname,lvl from questions")
        
        for qid,qname,lvl in cur:
            print(str(qid)+"\t"+qname+"\t"+lvl)
        self.edit_question(cur,cur1,con)
    
        con.commit()
    def edit_question(self,cur,cur1,con):
        print("Enter Question Number/Category/ALL:")
        choice=input()
        try:
            if(choice.isdigit()):
                cur.execute("select qid,category,qname,lvl from questions where qid='"+str(choice)+"'")
                print(" ")
                self.update_que(cur,cur1,con,choice)
            elif(choice=='Movie' or choice=='Country'):
                cur.execute("select qid,category,qname,lvl from questions where category='"+choice+"'")
                print(" ")
                self.update_que(cur,cur1,con,choice)
            
            elif(choice=='All'):
                cur.execute("select qid,category,qname,lvl from questions")
                print(" ")
                self.update_que(cur,cur1,con,choice)
            else:
                raise exceptions.InvalidOptionSelection
        except exceptions.InvalidOptionSelection as e:
            print (e)
        con.commit()
    def update_que(self,cur,cur1,con,choice):    
        
        for row in cur:
            print("Old question :",row[2])
            print("New question")
            
            new_que=input()
            try:    
                print("Old Category :",row[1])
                print("New Category")
            
                new_cat=input()
                if(new_cat!="Movie" and new_cat!="Country"):
                    raise exceptions.InvalidCategoryException
                
                print("Old level :",row[3])
                print("New Level")
                new_lvl=input()
                if(new_lvl!="Easy" and new_lvl!="Medium" and new_lvl!="Hard"):
                    raise exceptions.InvalidLevelException
                cur1.execute("update questions set qname='"+new_que+"', category='"+new_cat+"', lvl='"+new_lvl+"' where qid = '"+str(row[0])+"'")   
                cur1.execute("insert into edited_q values('"+str(row[0])+"','"+new_que+"','"+new_lvl+"',systimestamp)")
                print("")
                print("Question updated")
        
            except exceptions.InvalidCategoryException as e:
                print(e)
            except exceptions.InvalidLevelException as e:
                print(e)
        self.get_values(cur,cur1,con)
        
        con.commit()
    
    def quick_update(self,cur,cur1,con, qid):
        for row in cur:
            print("Old question :",row[2])
            print("New question")
            
            new_que=input()
            try:    
                print("Old Category :",row[1])
                print("New Category")
            
                new_cat=input()
                if(new_cat!="Movie" and new_cat!="Country"):
                    raise exceptions.InvalidCategoryException
                
                print("Old level :",row[3])
                print("New Level")
                new_lvl=input()
                if(new_lvl!="Easy" and new_lvl!="Medium" and new_lvl!="Hard"):
                    raise exceptions.InvalidLevelException
                cur1.execute("update questions set qname='"+new_que+"', category='"+new_cat+"', lvl='"+new_lvl+"' where qid = '"+str(row[0])+"'")   
                cur1.execute("insert into edited_q values('"+str(row[0])+"','"+new_que+"','"+new_lvl+"',systimestamp)")
                print("")
                print("Question updated")
        
            except exceptions.InvalidCategoryException as e:
                print(e)
            except exceptions.InvalidLevelException as e:
                print(e)
        con.commit()
    
    