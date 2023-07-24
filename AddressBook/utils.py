from regex import match

def is_valid_date(date:str):
    """ Date format "Day-Month-Year" """
    # Defining a template for a date in the "day-month-year" format
    pattern = r"\d{2}-\d{2}-\d{4}"
    
    # We use match() to check whether the string matches the template completely
    if match(pattern, date):
        # Additionally, we check that the entered date is a real date using datetime
        from datetime import datetime
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return True
        except ValueError:
            return False
    else:
        return False
    
    
   
def is_valid_number(num:str):
    
    """function to check the correct number format"""
    
    if not isinstance(num,str):
        
        return False
    
    if len(num) != 9 or  num[0] != '0':
        return False
    
    return True



def is_valid_email(email:str):
    
    """function to check the correct email format"""
    #   Defining a template for an email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # We use match() to check if the string matches the pattern completely
    if match(pattern, email):
        return True
    else:
        return False

