from utility import DBConnectivity
def check_password():
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("select id,password from admin")
        for id,passw in cur:
            passwd=passw
            #print(passwd)
        return passwd
    #except DatabaseError as e:
        #print(e)
        
    finally:   
        cur.close()
        con.commit();
        con.close()
    
def change_confirm_password(g):
    try:
        con = DBConnectivity.create_connection()
        cur = DBConnectivity.create_cursor(con)
        cur.execute("Update admin SET password=:pass where ID=:id",{"id":1,"pass":g})
    finally:    
        cur.close()
        con.commit();   
        con.close()