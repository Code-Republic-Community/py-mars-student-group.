from address_book.address_book import AddressBook
from address_book.file_handler import FileHandler
import os
import sys
import json


def get_data_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    return os.path.join(data_dir, filename)


def main():
    data_file_path = get_data_file_path("address_book_data.json")
    my_address_book = AddressBook()
    file_handler = FileHandler()
    if os.path.getsize(data_file_path) != 0:
        file_handler.load_address_book(my_address_book, data_file_path)
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
            file_handler.save_address_book(my_address_book, data_file_path)
            break
        else:
            print("You must enter one number from the list.")
            continue


if __name__ == "__main__":
    main()

































