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


def name_inpit():
    min_lenght_name = 2
    while True:
        name  = input("Enter name (or ' exit ', to exit) (count char > 1) -  ")
        if name == "exit":
            return None
        if (len(name) < min_lenght_name ):
            print("Enter agin")
        
        else:
            return name
        

def phone_number_input():
    while True:
        number = input("Enter Phone number (or ' exit ', to exit) (e.g. 0XXXXXXXXX) -")
        if number == "exit":
            return None
        if not is_valid_number(number):
            print("Enter agin")
        
        else:
            return number
    

def email_input():
    while True:
        email = input("Enter email (or ' exit ', to exit) ( e.g. name@gmail.com) - ")
        if email == "exit":
            return None
        if not is_valid_email(email):
            print("Enter agin")
        else:
            return email


def birthday_input():
    while True:
        birthday = input("Enter birthday (or ' exit ', to exit) (e.g. dd-mm-year)")
        if birthday == "exit":
            return None
        if not is_valid_date(birthday):
            print("enter agin")
        
        else:
            return birthday
        

def selectin(sels):
    print("Choose one of the options")
    index = 1
    for i in sels:
        print(f"{index})   {i}")
        index += 1
    
    while True:
        sel = input("Choose index - (or ' exit ', to exit) ")
        if sel == "exit":
            return None
        sel = int(sel)
        
        if sel<1 or sel > len(sels):
            print("Choose agin")
        
        else:
            return sels[sel-1]
        
