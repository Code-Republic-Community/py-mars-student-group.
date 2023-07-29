import os
import uuid
from address_book.utils import validate_email, validate_phone_number
from address_book.address_book import AddressBook
from address_book.contact import Contact
from address_book.file_handler import save_address_book, load_address_book

def main():
    address_book_filename = "data/address_book_data.json"

    if os.path.exists(address_book_filename):
        address_book = load_address_book(address_book_filename)
    else:
        address_book = AddressBook()

    while True:
        print("\nAddress Book Management System")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Save Address Book")
        print("6. Show All Contacts")
        print("7. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            surname = input("Enter the surname: ")
            phone_number = input("Enter the phone number (in 0XX-XXX-XXX format): ")

            if not validate_phone_number(phone_number):
                print("Invalid phone number format. Contact not added.")
                continue

            email = input("Enter the email address (ex. myemail@email.com): ")

            if not validate_email(email):
                print("Invalid email format. Contact not added.")
                continue

            additional_info = input("Enter additional info (optional): ")




            contact_id = str(uuid.uuid4())

            contact = Contact(contact_id, name, surname, phone_number, email, additional_info)
            address_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == "2":
            keyword = input("Enter search keyword: ")
            results = address_book.search_contact(keyword)
            if results:
                print("Search results:")
                for contact in results:
                    print(contact)
            else:
                print("No matching contacts found.")

        elif choice == "3":
            contact_id = input("Enter the ID of the contact to update: ")
            name = input("Enter the new name (leave empty to skip): ")
            phone_number = input("Enter the new phone number (leave empty to skip): ")
            email = input("Enter the new email address (leave empty to skip): ")
            additional_info = input("Enter new additional info (leave empty to skip): ")

            contact = address_book.get_contact_by_id(contact_id)
            if contact:
                contact.update_contact(name=name, phone_number=phone_number, email=email, additional_info=additional_info)
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

            if address_book.update_contact(name, phone_number=phone_number, email=email, additional_info=additional_info):
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == "4":
            id = input("Enter the ID of the contact to delete: ")
            if address_book.delete_contact(id):
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == "5":
            save_address_book(address_book_filename, address_book)
            print("Address book saved successfully!")

        elif choice == "6":
            if not address_book.contacts:
                print("No contacts found.")
            else:
                print("All Contacts:")
                for contact in address_book.contacts:
                    print(contact)

        elif choice == "7":
            answer = input("Do you want to exit? All unsaved info will be lost.\nType 'y' to confirm: ")

            if answer.lower() == 'y':
                break
            else:
                pass

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
