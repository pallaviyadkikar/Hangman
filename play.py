om exceptions import exceptions
from classes import Player
from utility import ShowGraphics
import random
from classes import Questions


class play:
    
    def play_by_leader(self,cat,name,city,cur,con):
        try:
            
            player_list=[]
            player_list1=[]
            count1=0
            '''Existing user checking'''
            cur.execute("select pname,category,points,city from player where pname='"+name+"' and city='"+city+"'") 
            for pname1,category1,points1,city1 in cur:
                player=Player()
                player.set_pname(pname1)
                player.set_category(category1)
                player.set_pname(points1)
                player.set_pname(city1)
                player_list.append(player)
                
            '''New user checking'''
            cur.execute("select pname,category,points,city from player where pname='"+name+"'") 
            for pname1,category1,points1,city1 in cur:
                player=Player()
                player.set_pname(pname1)
                player.set_category(category1)
                player.set_pname(points1)
                player.set_pname(city1)
                player_list1.append(player)
                
        
            if (len(player_list)==0):
                cur.execute("insert into player values ('"+name+"', '"+cat+"',0, '"+city+"')")
                self.play(cat,name,cur,con)
            if (len(player_list1)!=0):
                for i in player_list1:
                    if i.get_categoryy()==cat:
                        count1+=1
                if count1!=1:
#                     cur.execute("insert into player values ('"+name+"', '"+cat+"',0, '"+city+"')")
                    self.play(cat,name,cur,con)
                
            else:
                raise exceptions.invalid_name
        
        except exceptions.invalid_name:
            print("Choose correct option or change Name as name already exits in db")
            self.play_by_leader(name,city,cur,con)
        except Exception as e:
            print(e)
       
      
            
            
            
            
    def play_login(self,cur,con):
        try:
            
            count1=0
            choice1=input("New Player or Existing Player (N/E)?")
            choice1=choice1.upper()
            if choice1 not in ('N','E'):
                
                raise exceptions.input_play_login
            input_name=input("What is your name? ")
            input_city=input("What is your city? ")
            player_list=[]
            player_list1=[]
            count1=0
            '''Existing user checking'''
            cur.execute("select pname,category,points,city from player where pname='"+input_name+"' and city='"+input_city+"'") 
            for pname1,category1,points1,city1 in cur:
                player=Player.Player()
                player.set_pname(pname1)
                player.set_category(category1)
                player.set_pname(points1)
                player.set_pname(city1)
                player_list.append(player)
                
            '''New user checking'''
            cur.execute("select pname,category,points,city from player where pname='"+input_name+"'") 
            for pname1,category1,points1,city1 in cur:
                player=Player.Player()
                player.set_pname(pname1)
                player.set_category(category1)
                player.set_pname(points1)
                player.set_pname(city1)
                player_list1.append(player)
            if((choice1=='N' and len(player_list1)==0)):
                
                print("Choose category:")
                print("    1.Country")
                print("    2.Movies")
                print("    3.Exit")
                
                input_cate=input()
                
                if input_cate.isdigit()==True and input_cate in ('1','2','3'):
                    if ((choice1=='N' or choice1=='n') and input_cate=='1'):
                        cur.execute("insert into player values ('"+input_name+"','Country',0, '"+input_city+"')")
                        
                    elif ((choice1=='N' or choice1=='n') and input_cate=='2'):
                        cur.execute("insert into player values ('"+input_name+"','Movie',0,'"+input_city+"')")
                                        
                    if input_cate=='1':
                        values='Country'
                    elif input_cate=='2':
                        values='Movie'
                    elif input_cate=='3':
                        raise exceptions.Finish
                    self.play(values,input_name,cur,con)
                else:
                    raise exceptions.invalid_integer
                    
            elif((choice1=='E' and len(player_list)!=0)  and 
            len(input_name)>0 and input_name.isdigit()==False 
            and len(input_city)>0 and input_city.isdigit()==False):
            
                print("Choose category:")
                print("    1.Country")
                print("    2.Movie")
                print("    3.Exit")
                
                input_cate=input()
                
                if input_cate.isdigit()==True and input_cate in ('1','2','3'):
                    
                    if(input_cate=='1'):
                        category='Country'
                    elif(input_cate=='2'):
                        category='Movie'
                    elif(input_cate=='3'):
                        raise exceptions.Finish
                else:
                    raise exceptions.invalid_integer
                for i in player_list:
                    if(i.get_category()==category):
                        count1+=1
                if count1!=1:
                    cur.execute("insert into player values ('"+input_name+"', '"+category+"',0, '"+input_city+"')")
              
                self.play(category,input_name,cur,con)
                con.commit()
            else:
                raise exceptions.invalid_name
                    
                    
        except exceptions.Finish:
            print("Finish")
            '''Menu()'''
        except exceptions.input_play_login:
            print("Only N or E is allowed")
            self.play_login(cur,con)
        except exceptions.invalid_name:
            print("Choose correct option or change Name as name already exits in db")
            self.play_login(cur,con)
        except exceptions.invalid_integer:
            print("only 1,2,3 can be given . start again")  
            self.play_login(cur,con)
     
            
            
            
            
    def select_seven(self,category,cur,con):
        
           
            list_e=[]
            list_m=[]
            list_h=[]
            list_all=[]
            
            cur.execute("select qid,qname,lvl,category from questions where lvl='Easy' and category=:ca",{"ca":category})
            for quesid,qname,qlevel,qcate  in cur:
                
                selected_question_e=Questions.Question()
           
               
                selected_question_e.set_qid(quesid)
                selected_question_e.set_qname(qname)
                selected_question_e.set_lvl(qlevel)
                selected_question_e.set_category(qcate)
                
                list_e.append(selected_question_e)
                
            cur.execute("select qid,qname,lvl,category from questions where lvl='Medium' and category=:ca",{"ca":category})
            for quesid,qname,qlevel,qcate in cur:
                
                selected_question_m=Questions.Question()
                selected_question_m.set_qid(quesid)
                selected_question_m.set_qname(qname)
                selected_question_m.set_lvl(qlevel)
                selected_question_m.set_category(qcate)
                
                list_m.append(selected_question_m)
                
            cur.execute("select qid,qname,lvl,category from questions where lvl='Hard' and category=:ca",{"ca":category})
            for quesid,qname,qlevel,qcate  in cur:
                
                selected_question_h=Questions.Question()
                selected_question_h.set_qid(quesid)
                selected_question_h.set_qname(qname)
                selected_question_h.set_lvl(qlevel)
                selected_question_h.set_category(qcate)
                
                list_h.append(selected_question_h)
            
            list_all.append(list_e)
            list_all.append(list_m)
            list_all.append(list_h)
            
            return list_all     
        
            
    def play(self,values,input_name,cur,con):
    
        try:
           
            list_selected_question=[]    
            
            list_questions=self.select_seven(values,cur,con)
            
            list_easy=list_questions[0]
            list_medium=list_questions[1]
            list_hard=list_questions[2]
          
    
            count1=0
            list1=[]
            while(count1<3):
                a=random.randrange(0,len(list_easy))
                
                if a not in list1:
                    list1.append(a)
                    list_selected_question.append(list_easy[a])
                count1+=1
                    
    
            count2=0
            list2=[]
            while(count2<2):
                
                b=random.randrange(0,len(list_medium))
                
                if b not in list2:
                    list2.append(b)
                    list_selected_question.append(list_medium[b])
                count2+=1
            count3=0
            list3=[]
            while(count3<2):
                
                c=random.randrange(0,len(list_hard))
                
                if c not in list3:
                    list3.append(c)
                    list_selected_question.append(list_hard[c])
                count3+=1
    
            ''' displaying PyAngman and asking for guess'''
            
            
            summ=0
            for k in list_selected_question:
                answer=k.get_qname()
                
                cur.execute("insert into points_calculation values ('"+str(k.get_qid())+"',NULL)")
               
                
                if k.get_lvl()=='Easy':
                    pointss=10
                if k.get_lvl()=='Medium':
                    pointss=15
                if k.get_lvl()=='Hard':
                    pointss=20
                
                ans_len=len(answer)
                hypen=""
                listqq=[]
                count_error=0
                ShowGraphics.show_hang_man(0)
                print('Answer: ',end='')
                for j in range(0,ans_len):
                    hypen+="_ "
                    
                    print('_ ',end='')
                print('') 
                  
                while (hypen.count("_ ")!=0):
                    alphabet_print=""
                    guess=input("Guess a letter (A-Z): ")
                    if guess=='0':
                        
                        cur.execute("update player set points=points+'"+str(summ)+"' where pname='"+input_name+"' and category='"+values+"'")
                        
                        raise exceptions.Exit_Play
                    '''transfer the control'''
                   
                   
                    while guess.isdigit()==True or len(guess)!=1 :
                        print("enter only alphabet")
                        guess=input("Guess a letter (A-Z): ")
                    
                    if guess.lower() not in answer.lower():
                        count_error+=1
                        ShowGraphics.show_hang_man(count_error)
                        if(2<count_error<=5):
                            hint=input("Do u want hint either Y/N?")
                            if(hint=='Y' or hint=='y'):
                                
                                if(count_error==3):
                                    print('Endswith...',answer[-1])
                                elif(count_error==4):
                                    print('second last...',answer[-2])
                                elif(count_error==5):
                                    print('startswith...',answer[0])
                            elif(hint=='N' or hint=='n'):
                                pass    
                        if count_error==6:
                            break
                    else:   
                        ShowGraphics.show_hang_man(count_error)    
                        listqq.append(guess.lower())  
                    for asd in answer.lower():
                        if asd in listqq:
                            alphabet_print+=asd+" "
                            
                        else:
                            alphabet_print+="_ "
                    hypen=alphabet_print[0].upper() +alphabet_print[1:]
                    print('Answer: ',end='')
                    print(hypen)        
                if count_error==6:
                    print("Game over")
                    break
                else:
                    pointss=pointss-count_error
                    summ+=pointss
                    cur.execute("insert into points_calculation values ('"+str(k.get_qid())+"',1)")
                    print("Congrats, here's the next one:")
                    
            print("Hello %s You Scored: %d" %(input_name,summ)) 
#             cur.execute("update player set points=points+'"+str(summ)+"' where pname='"+input_name+"' and category='"+values+"'")  
            cur.execute("select points from player where pname='"+input_name+"' and category='"+values+"'")
            fetch_points=cur.fetchall()
            for row in fetch_points:
                for i in row:
                    if i<summ:
                        cur.execute(" update player set points='"+str(summ)+"' where pname='"+input_name+"' and category='"+values+"'")
                    
            
                    
            con.commit()
                            
        except exceptions.Exit_Play:
            pass
        
    
    
    
        
   

