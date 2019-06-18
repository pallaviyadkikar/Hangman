
from utility import DBConnectivity
from cx_Oracle import DatabaseError
#from classes import playmodule
def get_city():
    try:
        listt=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT DISTINCT LOWER(E.CITY) FROM PLAY P INNER JOIN PLAYER E ON P.PNAME=E.PNAME")
        
        for i in cur:
            #print(i)
            listt.append(i[0])
            #print(listt)
        return listt
    except DatabaseError as e:
        print(e)
    finally:
        cur.close()
        con.close()
        
def get_name():
    try:
        listt=[]
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT DISTINCT LOWER(E.PNAME) FROM PLAY P INNER JOIN PLAYER E ON P.PNAME=E.PNAME")
        
        for i in cur:
            #print(i)
            listt.append(i[0])
            #print(listt)
        return listt
    except DatabaseError as e:
        print(e)
    finally:
        cur.close()
        con.close()
        
def get_city_desc(lcity):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT P.PNAME,P.POINTS FROM PLAY P INNER JOIN PLAYER E ON P.PNAME=E.PNAME WHERE LOWER(E.CITY)=:CITTY ORDER BY P.POINTS DESC",{"CITTY":lcity})
        COUNT=1
        for PNAME,POINTS in cur:
            Y=str(COUNT)
            Z=str(POINTS)
            print(Y+"."+"\t"+PNAME+"\t\t"+Z)
            COUNT+=1
    except DatabaseError as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()
def get_category(player,categoryy):
    try:
        con=DBConnectivity.create_connection()
        cur=DBConnectivity.create_cursor(con)
        cur.execute("SELECT PNAME,POINTS,CATEGORY FROM(SELECT PNAME,POINTS,CATEGORY FROM PLAY WHERE LOWER(CATEGORY)=:CATT ORDER BY POINTS DESC) WHERE ROWNUM<=:VAL",{"CATT":categoryy.lower(),"VAL":player})
        print("======================================================")
        print("Top "+player+" player in category "+categoryy)
        print("======================================================")
        for pname,points,category in cur:
            print(pname+"\t\t"+str(points)+"\t\t\t"+category)   
    except DatabaseError as e:
        print(e)
    finally:
        cur.close()
        con.commit()
        con.close()

   


