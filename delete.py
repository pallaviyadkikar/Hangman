
from exceptions import exceptions

class delete:   
    
    def delete(self,cur,con,cur1,option):
    
        print(option)
        choice_loop='Y'
        while(choice_loop=='Y'):
            
            if (option.startswith("delete")):
                if option!="delete":
                    l1=option.split(" ")
                    print(l1)
                    num=int(l1[1])
                    cur.execute("select qname,lvl,category from questions where qid=:n",{"n":num})
                    for row in cur:
                        print("question:",row[0])
                        print("level:",row[1])
                        print("category:",row[2])
                    inp=input("DELETE Y/N")
                    if inp.upper()=="Y": 
                       
                        cur.execute("DELETE FROM points_calculation  WHERE qid=:n",{"n":num})
                        cur.execute("DELETE FROM added_q  WHERE qid=:n",{"n":num})
                        cur.execute("DELETE FROM edited_q  WHERE qid=:n",{"n":num})
                        cur.execute("DELETE FROM questions  WHERE qid=:n",{"n":num})
                        
                           
                      
                        print("Question deleted")
                        print("=================================")
                    
                    elif inp.upper()=="N":
                        return
                
                
                else:
                    
                    category1=input("Category:")
                    level=input("level:")
                    qname=input("Question:")
                    print("============================================================")
                    
                    cur.execute("select * from  questions")    
                        
                    try:
                           
                        if category1=='' and level=='' and qname=='':
                                
                                for row in cur:
                                    for i in row:
                                        print(str(i),end=' ')
                                    print("\n")  
                                self.enter_id(cur,cur1,con)
                        elif level in ('Hard','Medium','Easy') and category1 in ('Movie','Country') and qname=='':
                            
                                for row in cur:
                                    if row[3]==category1 and row[2]==level:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')
                                            print("\n") 
                                        else:
                                            raise exceptions.NoDataException 
                                self.enter_id(cur,cur1,con)
                                        
                        elif level in ('Hard','Medium','Easy') and category1=='' and qname=='':
                            
                                for row in cur:
                                    if row[2]==level:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')
                                            print("\n") 
                                        else:
                                            print("No data") 
                                self.enter_id(cur,cur1,con)
                                       
                                                #raise exceptions.NoDataException
                                            
                        elif level =='' and category1 in ('Movie','Country') and qname=='':
                                    
                                for row in cur:
                                    if row[3]==category1:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')
                                            print("\n")  
                                        else:
                                            raise exceptions.NoDataException
                                self.enter_id(cur,cur1,con)
                                        
                        elif level =='' and category1=='' and qname!='':
                                    
                                for row in cur:
                                    if qname.lower()   in row[1].lower():
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')
                                            print("\n") 
                                        else:
                                            raise exceptions.NoDataException 
                                self.enter_id(cur,cur1,con)
                                       
                        elif level in ('Hard','Medium','Easy') and category1=='' and qname!='':
                                    
                                for row in cur:
                                    if qname.lower()  in row[1].lower() and row[2]==level:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ') 
                                            print("\n")       
                                        else:
                                            raise exceptions.NoDataException        
                                self.enter_id(cur,cur1,con)
                                        
                                                                     
                        elif level in ('Hard','Medium','Easy') and category1 in ('Movie','Country') and qname!='':
                                    
                                for row in cur:
                                    if qname.lower()  in row[1].lower() and row[2]==level and row[3]==category1:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')         
                                            print("\n")  
                                           
                                        else:
                                            raise exceptions.NoDataException
                                self.enter_id(cur,cur1,con)       
                        elif level=='' and category1 in ('Movie','Country') and qname!='':
                                    
                                for row in cur:
                                    if qname.lower()  in row[1].lower() and row[3]==category1:
                                        if row is not None:
                                            for i in row:
                                                print(str(i),end=' ')
                                            print("\n")  
                                            
                                        else:
                                            raise exceptions.NoDataException
                                self.enter_id(cur,cur1,con)
                    except exceptions.NoDataException as e:
                        print(e)
                                       
                      
            choice_loop=input("Do you want to search again?")        
                                   
        con.commit()               
    def enter_id(self,cur,cur1,con):
        l1=[] 
        l2=[]
        list1=[]
        input_choice=input("\n Enter Id(s) to Delete:")
        cur.execute("select qid from questions")
#         id=cur.fetchall()
#         for row in id:
#             list1.append(row[0])
#         cur.execute("Select qid from questions where qid in (%s)"%",".join(map(str,list1)))
#         
#         flag=0
#         for row in cur:
#             for j in row:
#                 
#                 if(input_choice==int(j)):
#                    
#                     flag=1
#                 break
#         if(flag==1):
        try:
            l2=input_choice.split(",")
            
            for item in l2:
                if (item.isdigit()):
                    cur.execute("select qname,lvl,category from questions where qid=:n",{"n":item})
                    #data=cur.fetchone()
        
                    #if data is None:
                     #   raise exceptions.NoIdFound
                    #else:
                    for row in cur:
                        print("question:",row[0])
                        print("level:",row[1])
                        print("category:",row[2])
                        input_confirm=input("DELETE Y/N")
                        if input_confirm=="Y":
                            cur1.execute("DELETE FROM points_calculation  WHERE qid=:n",{"n":item})
                            cur1.execute("DELETE FROM added_q  WHERE qid=:n",{"n":item})
                            cur1.execute("DELETE FROM edited_q  WHERE qid=:n",{"n":item})
                            cur1.execute("DELETE FROM questions  WHERE qid=:n",{"n":item})
                            print("Question deleted")
                        elif input_confirm=="N":
                            pass
                else:
                    print("Invalid Id")
            con.commit() 
        except exceptions.NoIdFound as e:
            print(e) 