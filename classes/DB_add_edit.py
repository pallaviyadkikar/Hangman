
from utility import DBConnectivity
from validations import add_edit_validations
from classes import DataStructures
from exceptions import add_edit_exceptions, delete_exceptions


        
def get_using_categories(edit_inp):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        if(add_edit_validations.validate_category(edit_inp)):
            cur.execute("SELECT QID,QUESTION,LEVELS FROM question where lower(category)=:cname",{"cname":edit_inp.lower()})
            for qid,question,levels in cur:
                print(str(qid)+"\t\t "+question+"   "+levels) 
        else:
            raise add_edit_exceptions.Category
        
    except add_edit_exceptions.Category as e: 
        print("working")
        print(e)
        '''refer exception creation'''
    finally:    
        cur.close()
        con.commit();
        con.close()    
        
def get_using_qid(edit_inp):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT QUESTION,CATEGORY,LEVELS FROM question where Qid=:qid",{"qid":edit_inp})
        for quest,cat,lvl in cur: 
            print("Old Question: "+quest)
            nq=input("New Question:");
            #print(cat)
            print("Old Category:"+cat)
            nc=input("New Category:");
            print("Old Level: "+lvl)
            nl=input("New Level:");
            print("Question Updated.")
            
        if(nq!=""):
            update_question(edit_inp,nq)
            update_edit_status(edit_inp)
        if(nc!=""):
            if(add_edit_validations.validate_category(nc)):
                update_category(edit_inp,nc)
                update_edit_status(edit_inp)
            else:
                raise add_edit_exceptions.Category
        if(nl!=""):
            if(add_edit_validations.validate_level(nl)):
                update_level(edit_inp,nl)
                update_edit_status(edit_inp)
            else:
                raise delete_exceptions.NoLevel 
        '''else:
            raise delete_exceptions.QuestionIDInvalid''' 
                 
    except add_edit_exceptions.QuestionID as e:
        print(e)
        '''refer exception creation'''
    finally:        
        cur.close()
        con.commit();
        con.close()
        
def get_all():
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT QID,QUESTION,CATEGORY,LEVELS FROM question")
        print("QID\t\tQUESTION\t\tCATEGORY\tLEVEL")
        for qid,question,category,levels in cur:
            print(str(qid)+"\t\t "+question+"\t\t\t"+category+"\t\t"+levels)            
    finally:
        cur.close()
        con.commit();
        con.close()
        
def update_question(edit_inp,nq):  
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("UPDATE question SET QUESTION=:ques WHERE QID=:qid",{"qid":edit_inp,"ques":nq})
     
    cur.close()
    con.commit();
    con.close()
        
def update_category(edit_inp,nc):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("UPDATE question SET CATEGORY=:cat WHERE QID=:qid",{"qid":edit_inp,"cat":nc})
  
    cur.close()
    con.commit();
    con.close()
    
def update_level(edit_inp,nl):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("UPDATE question SET LEVELS=:lev WHERE QID=:qid",{"qid":edit_inp,"lev":nl})
    
    cur.close()
    con.commit();
    con.close()
        
               
def add_question(nq1,nc1,nl1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT MAX(QID) FROM question")
        for qid in cur:
            maxid=qid[0];
        cur1=DBConnectivity.create_cursor(con)
        if(add_edit_validations.validate_category(nc1)):
            if(add_edit_validations.validate_level(nl1)):
                cur1.execute("Insert into question(QID,QUESTION,CATEGORY,LEVELS,NO_OF_ATTEMPTS,SUCCESS_ATTEMPTS) VALUES (:a,:b,:c,:d,0,0)",{"a":maxid+1,"b":nq1,"c":nc1,"d":nl1})                  
                print("Question Added with id "+str(maxid+1))
            else:
                raise delete_exceptions.NoLevel
        else:
            raise delete_exceptions.CategoryInvalid
        cur1.close()
    
    except delete_exceptions.CategoryInvalid as e:
        print(e)
        '''refer exception creation'''
    except delete_exceptions.NoLevel as e:
        print(e)
        '''refer exception creation'''            
    finally:
        cur.close()
        con.commit();
        con.close()
        
    return maxid

def update_edit_status(edit_inp):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("UPDATE question SET STATUS=:stat WHERE QID=:qid",{"qid":edit_inp,"stat":'E'})
    
    cur.close()
    con.commit();
    con.close()

def recently_edited(stack1):
    count=1
    stk2=DataStructures.Stack(50) 
    while(not stack1.is_empty()):
        if(count<=5):        
            var=stack1.pop()
            select_using_id_edit();
            stk2.push(var)
            count+=1
            print(stk2)
    while(not stk2.is_empty()):
        stack1.push(stk2.pop())
            
def recently_added(stack2):
    stack2.display()
    count=1
    stk2=DataStructures.Stack(50) 
    while(not stack2.is_empty()):
        if(count<=5):        
            var=stack2.pop()
            select_using_id_add();
            stk2.push(var)
            count+=1
            print(stk2)
    while(not stk2.is_empty()):
        stack2.push(stk2.pop())
   
        
'''def select_using_id(id1):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    cur.execute("SELECT QID,QUESTION,LEVELS FROM question where Qid=:qid",{"qid":id1})
    for qid,question,levels in cur:
        print(str(qid)+"\t"+question+"\t\t"+levels)   
    
    cur.close()
    con.commit();
    con.close();'''

def select_using_id_add():
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    #count=0
    #while(count<5):
    cur.execute("SELECT QID,QUESTION,LEVELS FROM(SELECT QID,QUESTION,LEVELS FROM question where status=:stat order by time_stamp desc) where rownum<6",{"stat":'A'})
    #where status=:stat and rownum<6 ,,{"stat":'A'}
    for qid,question,levels in cur:
        print(str(qid)+"\t"+question+"\t\t"+levels)  
        #count+=1 
    
    cur.close()
    con.commit();
    con.close();

def select_using_id_edit():
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    #count=0
    #while(count<5):
    cur.execute("SELECT QID,QUESTION,LEVELS FROM(SELECT QID,QUESTION,LEVELS FROM question where status=:stat order by time_stamp desc) where rownum<6",{"stat":'E'})
    #where status=:stat and rownum<6 ,,{"stat":'A'}
    for qid,question,levels in cur:
        print(str(qid)+"\t"+question+"\t\t"+levels)  
        #count+=1 
    
    cur.close()
    con.commit();
    con.close();
        
def get_questionids():
    
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    id_list1=[]
    id_list=[]
    str1=""
    cur.execute("Select Qid from question")
    for ids in cur:
        id_list1.append(ids[0])
    #for i in id_list1:
    #    str1+=str(i)
    #print(str1)
    #for i in str1:
        #id_list.append(i)
    
    return id_list1
