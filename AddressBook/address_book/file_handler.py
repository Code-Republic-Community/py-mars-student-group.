import json
from pymongo import MongoClient
from address_book.contact import Contact
import os


class MongoDBHandler:
    """
    The MongoDBHandler class provides methods to save and load address book data in a MongoDB database.
    Methods:
        save_address_book(self, my_address_book): Save address book data to a MongoDB collection.
        load_address_book(self, my_address_book): Load address book data from a MongoDB collection.
    """

    def __init__(self, database_name='mydatabase', collection_name='address_book'):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client[database_name]
        self.collection = self.db[collection_name]

    def save_contact(self, contact):
        """
        Save address book data to a MongoDB collection.
        """
        def strip_leading_underscore(contact_dict):
            return {key.strip('_'): value for key, value in contact_dict.items()}
        contact = strip_leading_underscore(vars(contact))
        self.collection.insert_one(contact)

    def change_contact(self, contact):
        """
        Update a contact in the MongoDB collection.s
        Parameters:
            contact (Contact): The contact object with updated fields.
        """
        def strip_leading_underscore(contact_dict):
            return {key.strip('_'): value for key, value in contact_dict.items()}
        updated_contact = strip_leading_underscore(vars(contact))
        self.collection.update_one({"tel_number": contact.tel_number}, {"$set": updated_contact})

    def load_address_book(self, my_address_book):
        """
        Load address book data from a MongoDB collection.
        """
        cursor = self.collection.find({})
        for contact_info in cursor:
            contact_info.pop("_id")
            my_address_book.contacts[contact_info["tel_number"]] = Contact(**contact_info)

    def delete_contact_from_db(self, tel_number):
        """
        Deletes a contact from the MongoDB collection based on the provided telephone number.
        """
        self.collection.delete_one({"tel_number": tel_number})
    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
