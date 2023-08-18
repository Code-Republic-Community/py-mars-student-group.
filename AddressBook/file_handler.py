import json
from AddressBook.address_book import Address_Book
import os
from  os import listdir
from pymongo import MongoClient



def create_address_book(adress_book,file_name):
    
    cotacts = []
    for i in adress_book.contacts:
        cotacts.append(adress_book.contacts[i].to_json())
    
    
    with open("data/"+file_name+".json", "w") as file:
        json.dump(cotacts, file)
    
    print("address book created")
    
    

def read_address_book():

    
    file_names = listdir("data/")
    address_book = Address_Book()
    
    
    while True:
        index = 1
        for i in file_names:
            print(f"{index})  {i} ")
            index +=1
        j = input("Enter index for file name (or ' exit ', to exit): - ")
        if j == "exit":
            return None
        j= int(j)
        
        
        if j<0 or j > len(file_names):
            print("select again")
        else:
            file_name = file_names[j-1]
            
        
        
            with open("data/"+file_name, "r") as file:
                data = json.load(file)
    
            for contact in data:
                address_book.add_contact(contact["name"],contact["phone_number"],contact["email_address"],contact["birthday"])
        
            
            return address_book

         

def delete_address_book():
    file_names = listdir("data/")
   
    
    while True:
        index = 1
        for i in file_names:
            print(f"{index})  {i} ")
            index +=1
        j = input("Enter index for file name (or ' exit ', to exit): - ")
        if j == "exit":
            return None
        
        j = int(j)
        
        if j<0 or j > len(file_names):
            print("select again")
        else:
            file_name = file_names[j-1]
            os.remove("data/"+file_name)
            break
        
        
def add_addressBook_DB(address_book):
    
    client = MongoClient('localhost', 27017)
    db = client["mydatabase"]
    collection = db["New_a_b"]
    for contact in address_book.contacts.values():
        collection.insert_one(contact.to_json())
    
    print(" Address Book Inserted !")
    
    

def import_address_book():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['New_a_b']

    data = collection.find()  

    new_address_book = Address_Book()
    for contact  in data:
        new_address_book.add_contact(contact["name"],contact["phone_number"],contact["email_address"],contact["birthday"]) 

    return new_address_book