import time
from file_handler import save_to_file, load_from_file
from utils import create_address_book , choose_address_book
def start():
    global address_books
    address_books = []
    actions = ["1 - Create Address Book", "2 - Choose Address Book", "3 - Add contact", "4 - Search contact", "5 - Update contact", "6 - Delete contact", "7 - Save Address Book to file", "8 - Load Address Book from file", "9 - Exit"]
    
    while True:
        time.sleep(1)
        for action in actions:
            print(action)

        action = input("Choose the action you want: ")

        if action == "1":
            create_address_book()

        elif action == "2":
            address_book = choose_address_book()
            print(f"Using address book: {address_book.name}")

        elif action == "3":
            address_book.add()

        elif action == "4":
            criteria = input("Enter the search criteria: ")
            address_book.search(criteria)

        elif action == "5":
            contact_detail = input("Enter the detail's value you want to update:")
            address_book.update(contact_detail)

        elif action == "6":
            contact_detail = input("You can enter any contact detail and delete the contact according to that detail: ")
            address_book.delete(contact_detail)

        elif action == "7":
            filename = input("Enter file name for saving Address Book to file: ")
            save_to_file(address_book, filename)

        elif action == "8":
            filename = input("Enter file name for loading Address Book from file: ")
            load_from_file(address_book, filename)
        
        elif action == "9":
            break
            
        else:
            print("Invalid action. Please choose a vaild action")



if __name__ == "__main__":
    start()
