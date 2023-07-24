from contact import Contact


class Address_Book:
    def __init__(self) -> None:
        self.contacts = {}
        
    def add_contact(self,name:str,phone_number:str,email_address:str,birthday:str) -> None:
        """
        Args:
            name (str): name user 
            phone_number (str): phone number user
            email_address (str): email address user 
            birthday (str): birthday  user "Day-Month-Year" 
            
        """
        
        new_contact = Contact(name,phone_number,email_address,birthday)
        
        self.contacts[new_contact.name] = new_contact
    
    
    
        

