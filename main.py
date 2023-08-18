from AddressBook import utils

from AddressBook.address_book import Address_Book


from AddressBook import file_handler



def main():
    address_book = Address_Book()
    
    while True:
        print("-----------------------------")
        print("Enter opration")
        print("1) Add contact")
        print("2) Delete contact ")
        print("3) Update contact")
        print("4) Search contact")
        print("5) Creat address book json file")
        print("6) load address book file")
        print("7) Delete address book file")
        print("8) Show all contacts")
        print("9) Inserting a document DB ")
        print("10)Import address book from DB")
        print("0) Exit")
        print("-----------------------------")
        
        sel = input(": - ")
        
        if sel == "1":
            name = utils.name_inpit()
            if name == None:
                    continue
                
            
            
            while True:
                number = utils.phone_number_input()
                
                
                
                if number not in  address_book.contacts:
                    
                    break
                
                print("the number already exists")
            
            if number == None:
                    continue
            
            while True:
                
                email = utils.email_input()
                
                
                
                j = 0
                for i in address_book.contacts.values():
                    if email == i.email_address:
                        j += 1
                if j > 0:
                    print("email already exists")
                else:
                    break
            
            if email == None:
                    continue
                
            birthday = utils.birthday_input()
            if birthday == None:
                    continue

            address_book.add_contact(name,number,email,birthday)
        
        elif sel == "2":
            while True:
                
                if len(address_book.contacts) == 0:
                    
                    print("address book empty")
                    break
            
                contact_list = []
                j = 0
                for contact in address_book.contacts.values():
                    contact_list.append(contact.phone_number)
                    print(j," - ",contact)
                    j +=1
                    
                
                i = input("Enter contact  to delete (or ' exit ', to exit): ")
                
                if i == "exit":
                    break
                
                i = int(i)
                
                if  j<i<0:
                    
                    print("Number not fond")
                    
                else:
                    print(address_book.contacts.pop(contact_list[i]))
                    print("Contact deleted")
                    break
                
        elif sel == "3":
            while True:
                
                if len(address_book.contacts) == 0:
                    
                    print("address book empty")
                    break
            
                contact_list = []
                j = 0
                for contact in address_book.contacts.values():
                    contact_list.append(contact.phone_number)
                    print(j," - ",contact)
                    j +=1
                    
                
                i = input("Enter contact  to update (or ' exit ', to exit): ")
                
                if i == "exit":
                    break
                
                i = int(i)
                
                if  j<i<0:
                    
                    print("Number not fond")
                    
                else:
                    update_contact = address_book.contacts[contact_list[i]]
                    
                    choose_list =["name","phone_number","email_address","birthday"]
                    update_parametr = utils.selectin(choose_list)
                    if update_parametr == None:
                        break
                    
                    if update_parametr == "name":
                        new_name = utils.name_inpit()
                        if new_name == None:
                            break
                        
                        address_book.update_contact(update_contact,update_parametr,new_name)
                        
                    elif update_parametr == "phone_number":
                        new_phone_number = utils.phone_number_input()
                        if new_phone_number == None:
                            break
                        
                        address_book.update_contact(update_contact,update_parametr,new_phone_number)
                        
                    elif update_parametr == "email_address":
                        new_email_address = utils.email_input()
                        if new_email_address == None:
                            break
                        address_book.update_contact(update_contact,update_parametr,new_email_address)
                    
                    elif update_parametr == "birthday":
                        new_birthday = utils.birthday_input()
                        if new_birthday == None:
                            break
                        address_book.update_contact(update_contact,update_parametr,new_birthday)
                    
                        
                    
                    break
        
        elif sel == "4":
            
            choose_list =["name","phone_number","email_address","birthday"]
            search_parametr = utils.selectin(choose_list)
              
            if search_parametr == "name" or search_parametr == "birthday":
                
                address_book.search_contact(search_parametr)
                
            
            elif search_parametr == "phone_number":
                
                found_nuber = address_book.search_contact(search_parametr)
                if found_nuber == None:
                    print("Nuber not found")
                else:
                    print("contact found")
                    print(address_book.contacts[found_nuber])
                
            elif search_parametr == "email_address":
                found_email = address_book.search_contact(search_parametr,None)
                if found_email == None:
                    print("Nuber not found")
                else:
                    print("contact found")
                    print(found_email)
            
            
                        
                        
        elif sel == "5":
            file_name = input(("enter a name for the file (or ' exit ', to exit): - "))
            
            if file_name == "exit":
                continue
            
            
            file_handler.create_address_book(address_book,file_name)
            
            
        
            
        elif sel == "6":
            
            new_address_book = file_handler.read_address_book()
            if new_address_book == None:
                break
            
            address_book = new_address_book
            
            print("Address book generated") 
        
        
        elif sel == "7":
            file_handler.delete_address_book()
            print("Address book deleted")
            
        
        elif sel == "8":
            for contact in address_book.contacts.values():
                print(contact)
            
        elif sel == "9":
            file_handler.add_addressBook_DB(address_book)
            
        elif sel == "10":
            address_book = file_handler.import_address_book()
            
        
        elif sel == "0":
            break
        
        else:
            print("select again")
            
    
        
if __name__ == "__main__":
    main() 
    
    


