from address_book.address_book import AddressBook
from address_book.file_handler import MongoDBHandler
import os
import sys
import json


def get_data_file_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, "data")
    return os.path.join(data_dir, filename)





def main():
    my_address_book = AddressBook()
    db_handler = MongoDBHandler(database_name='mydatabase', collection_name='address_book')

    if db_handler.collection.count_documents({}) != 0:
        db_handler.load_address_book(my_address_book)

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
            # db_handler.save_address_book(my_address_book)
            db_handler.close_connection()
            break
        else:
            print("You must enter one number from the list.")
            continue


if __name__ == "__main__":
    main()

# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017/')
# db = client['mydatabase']
# collection = db['address_book']
# for document in collection.find():
#     document.pop("_id")
#     print(document)
#
# client.close()


































