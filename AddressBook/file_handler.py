import json
from address_book import Address_Book

def create_address_book(adress_book):
    
    cotacts = []
    for i in adress_book.contacts:
        cotacts.append(adress_book.contacts[i].to_json())
    
    
    with open("data/address_book_data.json", "w") as file:
        json.dump(cotacts, file)
    
    print("address book created")
    
    

def read_address_book():
    
    address_book = Address_Book()
    
    with open("data/address_book_data.json", "r") as file:
        data = json.load(file)
    
    for contact in data:
        address_book.add_contact(contact["name"],contact["phone_number"],contact["email_address"],contact["birthday"])
        
        
    return address_book

         

