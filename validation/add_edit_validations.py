
def validate_category(category):
    if category.lower() in ('movies','country'):
        return True
    else:
        print("**INVALID CATEGORY")
        return False

def validate_level(level):
    if level.lower() in ('easy','medium','hard'):
        return True
    else:
        print("**INVALID LEVEL")
        return False



