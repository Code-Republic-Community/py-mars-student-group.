from address_book.address_book import AddressBook
from address_book.file_handler import FileHandler
import json


def main():
    my_address_book = AddressBook()
    file_handler = FileHandler()
    file_handler.load_address_book(my_address_book)
    while True:
        action = input("Enter 1 to add contact, 2 to search contact, 3 to delete contact, "
                       "4 to update contact, 0 to save Address Book and exit: ")
        if "1" == action.strip():
            my_address_book.add_contact()
        elif "2" == action.strip():
            my_address_book.search_contact()
        elif "3" == action.strip():
            my_address_book.delete_contact()
        elif "4" == action.strip():
            my_address_book.update_contact()
        elif "0" == action.strip():
            file_handler.save_address_book(my_address_book)
            break
        else:
            print("You must enter one number from the list.")
            continue


if __name__ == "__main__":
    main()





















