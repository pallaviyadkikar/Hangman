'

from utility import DBConnectivity 
from validations import delete_validations
from exceptions import delete_exceptions

def selectingrows_qid(id1): 
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
 
        cur.execute("select question,category,levels from question WHERE Qid=:q_id",{"q_id":id1})
        for qstn,cat,lvl in cur:
            print("Question: "+qstn)
            print("Category: "+cat)
            print("Level: "+lvl)
    
    finally:
        cur.close()
        con.commit();
        con.close()
        
def deleting_row(id1):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("DELETE FROM question WHERE Qid=:q_id",{"q_id":id1})
        print("Question Deleted.")
    finally:
        cur.close()
        con.commit();
        con.close()

def delete_question(cat,lvl,qstn):
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    if(cat=="" and lvl=="" and qstn!=""):
        cur.execute("Select Qid, question, levels, category from question WHERE question LIKE '%"+qstn+"%'");
        print("============================================")
        print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
        for  Qid, question, levels, category in cur:
            print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
        print("============================================")
            
    elif(cat=="" and lvl!="" and qstn==""):
        try:
            if(delete_validations.validate_level(lvl)):
                cur.execute("Select Qid, question, levels, category from question WHERE lower(levels)=:levl",{"levl":lvl.lower()});
                print("============================================")
                print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                for  Qid, question, levels, category in cur:
                    print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                print("============================================")
            else:
                raise delete_exceptions.NoLevel 
            
        except delete_exceptions.NoLevel as e:
            print(e)
            
        finally:
            con.commit();
        
    elif(cat!="" and lvl=="" and qstn==""):
        try:
            if(delete_validations.validate_category(cat)):
                cur.execute("Select Qid, question, levels, category from question WHERE lower(category)=:catgry",{"catgry":cat.lower()})
                print("============================================")
                print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                for  Qid, question, levels, category in cur:
                    print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                print("============================================")
            else:
                raise delete_exceptions.CategoryInvalid
            
        except delete_exceptions.CategoryInvalid as e:
            print(e)
            
        finally:
            con.commit();
        
    elif(cat!="" and lvl!="" and qstn==""):
        try:
            if(delete_validations.validate_category(cat)):
                if(delete_validations.validate_level(lvl)):
                    cur.execute("Select Qid, question, levels, category from question WHERE lower(category)=:catgry and lower(levels)=:levl",{"catgry":cat.lower(),"levl":lvl.lower()})
                    print("============================================")
                    print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                    for  Qid, question, levels, category in cur:
                        print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                    print("============================================")
                else:
                    raise delete_exceptions.NoLevel
            else:
                raise delete_exceptions.CategoryInvalid
            
        except delete_exceptions.CategoryInvalid as e:
            print(e)
        except delete_exceptions.NoLevel as e:
            print(e)
            
        finally:
            con.commit();
        
    elif(cat=="" and lvl!="" and qstn!=""):
        try:
            if(delete_validations.validate_level(lvl)):
                cur.execute("Select Qid, question, levels, category from question WHERE question LIKE '%"+qstn+"%' and lower(levels)=:levl",{"levl":lvl.lower()})
                print("============================================")
                print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                for  Qid, question, levels, category in cur:
                    print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                print("============================================")
            else:
                raise delete_exceptions.NoLevel
            
        except delete_exceptions.NoLevel as e:
            print(e)
            
        finally:
            con.commit();
        
    elif(cat!="" and lvl=="" and qstn!=""):
        try:
            if(delete_validations.validate_category(cat)):
                cur.execute("Select Qid, question, levels, category from question WHERE  question LIKE '%"+qstn+"%' and lower(category)=:catgry",{"catgry":cat.lower()})
                print("============================================")
                print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                for  Qid, question, levels, category in cur:
                    print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                print("============================================")
            else:
                raise delete_exceptions.CategoryInvalid
            
        except delete_exceptions.CategoryInvalid as e:
            print(e)
            
        finally:
            con.commit();
        
    elif(cat!="" and lvl!="" and qstn!=""):
        try:
            if(delete_validations.validate_category(cat)):
                if(delete_validations.validate_level(lvl)):
                    cur.execute("Select Qid, question, levels, category from question WHERE question LIKE '%"+qstn+"%' and lower(category)=:catgry and lower(levels)=:levl",{"catgry":cat.lower(),"levl":lvl.lower()})
                    print("============================================")
                    print("QID"+"\t"+"QUESTION"+"\t"+"LEVEL"+"\t"+"CATEGORY")
                    for  Qid, question, levels, category in cur:
                        print(str(Qid)+"\t"+question+"\t\t"+levels+"\t"+category)
                    print("============================================")
                else:
                    raise delete_exceptions.NoLevel
            else:
                raise delete_exceptions.CategoryInvalid
            
        except delete_exceptions.CategoryInvalid as e:
            print(e)
        except delete_exceptions.NoLevel as e:
            print(e)
            
        finally:
            con.commit();
            
    cur.close()
    con.close()

def get_questionids():
    
    con=DBConnectivity.create_connection()
    cur=DBConnectivity.create_cursor(con)
    id_list1=[]
    id_list=[]
    str1=""
    cur.execute("Select Qid from question")
    for ids in cur:
        id_list1.append(ids[0])
#     for i in id_list1:
#         str1+=str(i)
#     #print(str1)
#     for i in str1:
#         id_list.append(i)
    
    return id_list1

    