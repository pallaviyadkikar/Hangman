from functionality import play

from exceptions import CustomException
from validations.validations import validate_category
import functionality
""" displays top scores from the city provided and filter conditions are also specified.player has to choose accordingly"""


class leaderboard:
   
    
    def cal_count(self,cur):
        c=0
        for row in cur:
            c+=1
        return c
    def leader(self,con,cur):
       
        print("Enter your name:")
        name=input()
        print("Enter your city:")
        city=input()   
            
        cur.execute("select * from player where city='"+city+"' order by points desc")
        data=cur.fetchone()
            
        if data is None:
            print('No Players Found')
        else:
            print("=========================")
            print("Top Players from "+city.upper()+":")
            print("=========================")
            
            cur.execute("select * from player where city='"+city+"' order by points desc")    
            count=0
            for player in cur:
                count=count+1
                print(str(count)+" "+player[0]+" "+str(player[2])+" "+player[1])
                if count==5:
                    break
            print("===============================")
            status = input("Do you wish to apply filter (Y/N)?").upper()             
            
            
            
            flag=False
            valid = False
            flag1=True 
            no_of_players=0
            while(flag==False): 
                if(status=="Y"):                
                    if(flag1==True):  
                        no_of_players = input("No. of Players to be displayed(3-10)")
                        
                        if(no_of_players==''):
                            no_of_players=str(5)
                        if(int(no_of_players)>=3 and int(no_of_players)<=10):
                            print("category should be either Country or Movie")
                            category = input("category:")
                            try:
                                if(category!=''):
                                    validate_category(category,con,cur)
                                valid = True   
                                details = input("Details:") 
                            except CustomException.InvalidCategoryException as e:
                                print(e)
                                continue
                            finally:
                                if(valid==True):
                                    print("===============================")                   
                                    if(category!='' and details!=''):
                                        cur.execute("select * from player where category='"+category+"' order by points desc")
                                        count=0
                                        x=self.cal_count(cur)
                                        if int(no_of_players)>x:
                                            b=x
                                        else:
                                            b=int(no_of_players)
                                        print("Top "+no_of_players+" Players in Category "+category.upper())
                                        print("============================")
                                        cur.execute("select * from player where category='"+category+"' order by points desc")
                                        for player in cur:
                                            
                                            if count==b:
                                                break;
                                            count=count+1
                                            if details.lower()=='name':
                                                print(str(count)+" "+player[0])
                                            elif details.lower()=='points':
                                                print(str(count)+" "+str(player[2]))
                                            elif details.lower()=='name, points':
                                                print(str(count)+" "+player[0]," ",str(player[2]))
                                            elif details.lower()=='name, points, category':
                                                print(str(count)+" "+player[0]," ",str(player[2])," ",str(player[1]))
                                            elif details.lower()=='name, category':
                                                print(str(count)+" "+player[0]," ",str(player[1]))
                                            
                                            elif details.lower()=='all':
                                                print(str(count)+" "+player[0]+" "+category+" "+str(player[2]))
                                            else:
                                                print("***INVALID DETAILS")
                                                break;
                                    
                                    elif(category=='' and details!=''):
                                                   
                                    
                                        cur.execute("select * from player order by points desc")
                                        count=0
                                        x=self.cal_count(cur)
                                        if int(no_of_players)>x:
                                            b=x
                                        else:
                                            b=int(no_of_players)
                                        print("Top "+no_of_players+" Players in Category "+category.upper())
                                        print("============================")
                                        cur.execute("select * from player order by points desc")
                                        for player in cur:
                                            if count==b:
                                                break;
                                            count=count+1
                                            if details.lower()=='name':
                                                print(str(count)+" "+player[0])
                                            elif details.lower()=='points':
                                                print(str(count)+" "+str(player[2]))
                                            elif details.lower()=='name, points':
                                                print(str(count)+" "+player[0]," ",str(player[2]))
                                            elif details.lower()=='name, points, category':
                                                print(str(count)+" "+player[0]," ",str(player[2])," ",str(player[1]))
                                            elif details.lower()=='name, category':
                                                print(str(count)+" "+player[0]," ",str(player[1]))
                                            elif details.lower()=='all':
                                                print(str(count)+" "+player[0]+" "+category+" "+str(player[2]))
                                            else:
                                                print("***INVALID DETAILS")
                                                break;       
                                            
                                            
                                    
                                    elif(category!='' and details==''):
                                        cur.execute("select * from player where category='"+category+"' order by points desc")
                                        count=0
                                        x=self.cal_count(cur)
                                        if int(no_of_players)>x:
                                            b=x
                                        else:
                                            b=int(no_of_players)
                                        print("Top "+no_of_players+" players in Category "+category.upper())
                                        print("============================")
                                        cur.execute("select * from player where category='"+category+"' order by points desc")
                                        for player in cur:
                                            if count==b:
                                                break;
                                            count=count+1
                                            print(str(count)+" "+player[0])
                                    elif(category=='' and details==''):
                                        cur.execute("select * from player order by points desc")
                                        count=0
                                        x=self.cal_count(cur)
                                        if int(no_of_players)>x:
                                            b=x
                                        else:
                                            b=int(no_of_players)
                                        print("Top "+no_of_players+" players in Category ")
                                        print("============================")
                                        cur.execute("select * from player order by points desc")
                                        for player in cur:
                                            if count==b:
                                                break;
                                            count=count+1
                                            print(str(count)+" "+player[0]+" "+player[1]+" "+str(player[2]))
                                    print("============================")
                                    if(category!=''):
                                        cur.execute("select * from player where category='"+category+"' order by points desc")
                                        x=self.cal_count(cur)
                                        if x==0:
                                            print('No Players Found')
                                        else:
                                            asss=input("Press 'P' to play this category or press any other to exit:").upper()
                                            if asss=='P':
                                                #p=play.play()
                                                play.play().play_by_leader(category,name,city,cur,con)  
                                                   
                                        return
                                    else:
                                        status = input("Do you wish to apply filter (Y/N)?").upper()
                                        if(status=='Y'):
                                            flag=False
                                            flag1=True
                                        elif status=='N':
                                            flag=True
                                        else:
                                            print("Enter valid choice in(Y/N)")
                                            input("Do yo wish to apply fliter again (Y/N)?").upper()
                                else:
                                    status = input("Do you wish to apply filter (Y/N)?").upper()
                                    if(status=='Y'):
                                        flag=False
                                        flag1=True
                                    elif status=='N':
                                        flag=True
                                    else:
                                        print("Enter valid choice in(Y/N)")
                                        input("Do yo wish to fliter again (Y/N)?").upper()
                        else:
                            print("Please enter no of players in specified range i,e between 3 and 10")
                            continue
                    else:                         
                        status = input("Do You Wish To Continue(Y/N)?").upper()
                        if(status == 'Y'):
                            flag=False                        
                            flag1=False
                        elif status=='N':
                            flag=True
                        else:
                            print("enter valid choice in(Y/N)")
                            input("Do yo wish to fliter again (Y/N)?").upper()
                elif status=='N':
                    return
                else:
                    print('Enter the valid choice in(Y/N)')
                    status=input("Do yo wish to fliter again (Y/N)?").upper()
                    flag=False
                    flag1=True
        con.commit()
       
                    
    
                  

