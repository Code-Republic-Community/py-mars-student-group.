from contact import Contact
from parameter_search import parameter_search


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
        if  new_contact.phone_number not in self.contacts:
        
            self.contacts[new_contact.phone_number] = new_contact
            print("contact added")
        
        else:
            print("the contact already exists")
        

        
    def dell_contact(self,contact):
        if contact is None:
            print("the contact does not exist")
        
        else:
            self.contacts.pop(contact.phone_number)
            print(f"contact deleted")
        
    
        
    def search_contact(self,type_parametr,parametr = None):
        if type_parametr.lower() == "name":
            found_parameters = []
            for i in self.contacts:
                if self.contacts[i].name == parametr:
                    found_parameters.append(self.contacts[i])
            return found_parameters                
            
        elif type_parametr.lower() == "phone_number":
            phone_numbers = []
            for i in self.contacts:
                phone_numbers.append(self.contacts[i].phone_number)
            
            found_parameters = parameter_search(phone_numbers)
            if len(found_parameters) == 0:
                print("parameters not found")
            else:
                return self.contacts[found_parameters[0]]
            
            
        elif type_parametr.lower() == "email_address":
            email_addreses = []
            for i in self.contacts:
                email_addreses.append(self.contacts[i].email_address)
            
            found_parameters = parameter_search(email_addreses)
            if len(found_parameters) == 0:
                print("parameters not found")
            else:
                for i in self.contacts:
                    if self.add_contact[i].email_address == found_parameters[0]:
                        return self.contacts[i]
                
        
        elif type_parametr == "birthday":
            found_parameters = []
            for i in self.contacts:
                if self.contacts[i].birthday == parametr:
                    found_parameters.append(self.contacts[i])
            return found_parameters
        
        
    def update_contact(self,contact,update_parametr_type,update_parametr):
        if update_parametr_type == "name":
            
            print(f"parametr  - {self.contacts[contact.phone_number].name} - update  -{update_parametr}")
            self.contacts[contact.phone_number].name = update_parametr
            
        elif update_parametr_type == "email_address":
            
            print(f"parametr  - {self.contacts[contact.phone_number].email_address} - update  -{update_parametr}")
            self.contacts[contact.phone_number].email_address = update_parametr
        
        elif update_parametr_type == "phone_number":
            
            print(f"parametr  - {self.contacts[contact.phone_number].phone_number} - update  -{update_parametr}")
            self.contacts[contact.phone_number].phone_number = update_parametr
            
        elif update_parametr_type == "birthday":
            
            print(f"parametr  - {self.contacts[contact.phone_number].birthday} - update  -{update_parametr}")
            self.contacts[contact.phone_number].birthday = update_parametr
        
    

