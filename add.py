from exceptions import exceptions

question_id=0

class add:
    
    
    def generate_q_id(self,cur,con):
    

        global question_id
        cur.execute("select * from questions")
        data=cur.fetchone()
    
        if data is None:
            question_id=100
        else:
            cur.execute("select qid from questions")
            for qid in cur:
                question_id=qid[0]

    
    
    def add_question(self,cur,con):
        self.generate_q_id(cur, con)
        global question_id
        cur.execute("select * from added_q")
        data=cur.fetchone()
        
        if data is not None:
            self.show_recent_items(cur,con)
            self.add_another_item(cur,con)
                
        else:
            print("No recent data added")
            self.add_another_item(cur,con)
                
        con.commit()
        
        end=True
            
    def show_recent_items(self,cur,con):
        count=0
        cur.execute("select q1.qid,q.qname,q.lvl from questions q inner join added_q q1 on q.qid=q1.qid order by add_time desc")
        print("Recently added Questions:")
        print("=============================")
        for qid,qname,lvl in cur:
            print(str(qid)+"\t"+qname+"\t"+lvl)
            count+=1
            if count==5:
                break         
    def add_another_item(self,cur,con):
        global question_id
        try:
            print("Category : ")
            category=input()
            if category!="Movie" and category!="Country":
                raise exceptions.InvalidCategoryException
            print("Question : ")
            question=input()
            print("Level : ")
            lvl=input()
            if lvl!="Easy" and lvl!="Medium" and lvl!="Hard":
                raise exceptions.InvalidLevelException
            question_id+=1
            
            cur.execute("insert into questions values('"+str(question_id)+"','"+question+"','"+lvl+"','"+category+"')")
            
            cur.execute("insert into added_q values('"+str(question_id)+"',systimestamp)")
        except exceptions.InvalidCategoryException as e:
            print(e)
    
        except exceptions.InvalidLevelException as e:
            print(e)   
        print("Do you want to add another?? Y or N")
        ans=input()
        if ans == "Y":
            self.add_question(cur,con)
            
        else:
            end=False     