from exceptions import CustomException
def validate_category(category,con,cur):
        
        cur.execute("select * from player where category='"+category+"'")
        data=cur.fetchone()
        
        if data is None:
                    
            raise CustomException.InvalidCategoryException(category)
            
        return cur