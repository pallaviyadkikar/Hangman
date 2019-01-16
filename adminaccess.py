
from exceptions import exceptions

login=False
class AdminAccess:
      
    def check_password(self,pwd,cur,con):
        cur.execute("select password from admin")
        
        password=cur.fetchone()
        if password[0]==str(pwd):
            return True
        else:
            return False
        
    def change_password(self,cur,con):
      
        try:
            print("Old password:")
            old_pwd=input()
            if self.check_password(old_pwd,cur,con)==True:
                print("New Password:")
                new_pwd=input()
                print("Confirm Password:")
                confirm_pwd=input()
                if new_pwd==confirm_pwd:
                    cur.execute("update admin set password=('"+new_pwd+"')")
                    con.commit()
                    print("Password Changed.")
                
                else:
                    raise exceptions.InvalidPasswordException
            else:
                raise exceptions.InvalidPasswordException
            
        except exceptions.InvalidPasswordException as e:
            print(e)
            
        return
            
    def logout(self,cur,con):
        login=False
        print("logged out")
        self.admin_menu(cur, con)
        
    def admin_menu(self,cur,con):
        qids_tuple=()
        print ("PyAngMan Admin Menu:")
        print("Password:")  
        pwd=input()
        try:
            if self.check_password(pwd,cur,con):
                print("Login Successful")
                login=True
                print("===========================================")
           
                print("Action Items:")
    
                count_qid="select qid,count(qid),count(result) from points_calculation group by qid "
                qids_fetch="select qid from points_calculation group by qid"
            
                cur.execute(count_qid)
                count_qid1=cur.fetchall()
            
                cur.execute(qids_fetch)
                count_only_id=cur.fetchall()
            
                for row in count_only_id:
                    qids_tuple+=row
                
                    
                   
                easy=[];med=[];hard=[]
                easy1=[];med1=[];hard1=[]
                      
                for row1 in count_qid1:
                    percent=0
                    percent=(row1[2]*100)/row1[1]
                    
                    if percent>80:
                        easy.append(row1[0])
                        
                    elif percent>50 and percent<=80:
                        med.append(row1[0])
            
                    elif percent<=50:
                        hard.append(row1[0])
                        
                cur.execute("select qid from questions where qid not in (select qid from points_calculation) and lvl='Easy'")   
                easyone=cur.fetchall()
                
                for row in easyone:
                    easy1.append(row[0])  
             
                    
                cur.execute("select qid from questions where qid not in (select qid from points_calculation) and lvl='Medium'")   
                medone=cur.fetchall()
                
                for row in medone:
                    med1.append(row[0]) 
                    
                cur.execute("select qid from questions where qid not in (select qid from points_calculation) and lvl='Hard'")   
                hardone=cur.fetchall()
                
                for row in hardone:
                    hard1.append(row[0]) 
                if len(easy1)!=0:
                    if len(easy)!=0:        
                        print("\n Following questions seems Easy:")
                        cur.execute("select qid from questions where lvl!='Easy' and qid in (%s)"%",".join(map(str,easy)))
                        for j in cur:
                            for k in j:
                                easy1.append(k)
                        print(easy1)
                        for i in easy1:
                            print(str(i), end=', ') 
                    else:
                        print("\n Following questions seems Easy:")
                        for i in easy1:
                            print(str(i), end=', ')
                if len(med1)!=0:
                    if len(med)!=0: 
                        print("\n Following questions seems Medium:")
                        cur.execute("select qid from questions where lvl!='Medium' and qid in (%s)"%",".join(map(str,med)))
                        for j in cur:
                            for k in j:
                                med1.append(k)
                   
                        for i in med1:
                            print(str(i), end=', ') 
                    else:
                        print("\n Following questions seems Medium:")
                        for i in med1:
                            print(str(i), end=', ')
                if len(hard1)!=0:
                    if len(hard)!=0: 
                        print("\n Following questions seems Hard:")
                        cur.execute("select qid from questions where lvl!='Hard' and qid in (%s)"%",".join(map(str,hard)))
                        for j in cur:
                            for k in j:
                                hard1.append(k)
               
                        for i in hard1:
                            print(str(i), end=', ') 
                    else:
                        print("\n Following questions seems Hard:")
                        for i in hard1:
                            print(str(i), end=', ')
            else:
                print("Login unsuccessfull!!!")
                self.admin_menu(cur, con)
        except exceptions.LoginUnsuccessfulException as e:
            con.commit()
            print(e)
