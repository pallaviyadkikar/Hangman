from database import DB_Package

def confirm_password(Password):
    if(DB_Package.check_password()==Password):
        return True
    else:
        return False
    
def change_new_password(z,w):
    if(z.lower()==w.lower()):
        #g=w.lower();
        return True
    else:
        return False