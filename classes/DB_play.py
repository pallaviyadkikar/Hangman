from utility import DBConnectivity
def check_names(name):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("select Pname from Player")
        for Pname in cur:
            plyname=Pname[0];
            if(plyname.lower()==name.lower()):
                return True
                
            
        return False
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def update_new_player(name,city):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("insert into Player values(:namee,:cityy)",{"namee":name,"cityy":city})
        
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def update_new_play_entry(name,category,points):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("insert into Play(Pname,Category,Points) values(:namee,:categoryy,:pointss)",{"namee":name,"categoryy":category,"pointss":points})
        
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def select_questions_player(category,level):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("select qid,question from question where category=:categoryy and levels=:levell ",{"categoryy":category,"levell":level})
        
        list1=[]
        for i in cur:
            x=i[0]
            
            list1.append(x)
        return list1
    ##print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def fetch_question(i):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("select question from question where qid=:qidd",{"qidd":i})
        for i in cur:
            return i[0]
        
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def update_points(name,category,points1):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("update play SET Points=:pts where Pname=:namee and Category=:categoryy",{"namee":name,"categoryy":category,"pts":points1})
        
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def fetch_points(name,category):
    try:
        pt=0
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("select points from play where pname=:namee and category=:categoryy",{"namee":name,"categoryy":category})
        for i in cur:
            pt=i[0]
            
        return pt
        
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
def fetch_attempts(qid):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("update question SET No_of_attempts=No_of_attempts+1 where qid=:qidd",{"qidd":qid})
        
            
    finally:   
        cur.close()
        con.commit();
        con.close()
def fetch_success_attempts(qid):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("update question SET success_attempts=success_attempts+1 where qid=:qidd",{"qidd":qid})
       
        
    finally:   
        cur.close()
        con.commit();
        con.close()
    
    