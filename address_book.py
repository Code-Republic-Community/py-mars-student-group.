import time
import json
import re
class AddressBook:
    """Class representing an address book."""
    def __init__(self, name):
        """Initialize the address book with a name and an empty list of contacts."""
        self.name = name
        self.contacts = []
    
    def add(self):
        """Add a new contact to the address book."""
        while True:
            name = input("Enter the contact's name: ")
            try:
                # Perform name validation (basic empty/whitespace check)
                if not name.strip():
                    raise ValueError("Name cannot be empty or contain only whitespace")
                break
            except ValueError as e:
                print(f"Invalid name: {e}")

        while True:
            phone_number = input("Enter the contact's phone number: ")
            try:
                # Validate phone_number format (only digits and dashes allowed)
                if not re.match(r'^[\d-]+$', phone_number):
                    raise ValueError("Invalid phone number format")
                break
            except ValueError as e:
                print(f"Invalid phone number: {e}")

        while True:
            email = input("Enter the contact's email: ")
            try:
                # Validate email format
                if not re.match(r'^[\w\.-]+@[\w\.-]+$', email):
                    raise ValueError("Invalid email format")
                break
            except ValueError as e:
                print(f"Invalid email: {e}")

        while True:
            birthday = input("Enter the contact's birthday: ")
            try:
                # Validate birthday format (let's assume YYYY-MM-DD)
                time.strptime(birthday, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid birthday format, use YYYY-MM-DD")

        contact = Contact(name, phone_number, email, birthday)
        self.contacts.append(contact)

    def search(self, criteria):
        """Search for contacts that match the given criteria and print the results."""
        found_contacts = []
        for contact in self.contacts:
            for key, value in contact.contact_dict.items():
                if criteria.lower() in value.lower():
                    found_contacts.append(contact)
                    break
                    
        if found_contacts:
            print("Matching contacts:")
            for contact in found_contacts:
                print(f"Name: {contact.contact_dict['name']}, "
                  f"Phone: {contact.contact_dict['phone_number']}, "
                  f"Email: {contact.contact_dict['email']}, "
                  f"Birthday: {contact.contact_dict['birthday']}")
                
        else:
            print("No contacts found matching the criteria.")

    def update(self, contact_detail):
        """Update the value of the given contact detail for selected contacts."""
        updated_contacts = []
        matching_contacts = []         #We create this list because contacts can have the same name or birthday                
        

        for contact in self.contacts:
            for key, value in contact.contact_dict.items():
                if contact_detail.lower() == value.lower():
                    matching_contacts.append(contact)
                    break

        if matching_contacts:
            print("Matching contacts:")
            for index, contact in enumerate(matching_contacts, 1):  
                print(f"{index} - {contact.contact_dict}")
        else:
            print("No contacts found matching the criteria.")


        while True:
            choice = input("Please select the contact number whose detail you want to change ")
            if choice.isnumeric():
                choice = int(choice)
                if 1 <= choice <= len(matching_contacts):
                    selected_contact = matching_contacts[choice - 1]
                    new_detail = input(f"Now enter new value for contact detail: ")
                    answer = input(f"Are you sure you want to change the contact's value?\nPlease answer YES or NO: ")

                    if answer.upper() == "YES":
                        for key in selected_contact.contact_dict.keys():
                            if selected_contact.contact_dict[key].lower() == contact_detail.lower():
                                selected_contact.contact_dict[key] = new_detail
                                break
                        updated_contacts.append(selected_contact)
                        print(f"Contact's detail '{contact_detail}' updated successfully.")
                    elif answer.upper() == "NO":
                        print("We will not update your data")
                    else:
                        print("Invalid input, please try again")
                    break
                else:
                    print("Invalid value. Please try again.")
            else:
                print("Invalid input. Please enter a number.")


    def delete(self, contact_detail):
        """Delete contacts based on the given contact detail."""
        deleted_contacts = []
        matching_contacts = []

        for contact in self.contacts:
            for key, value in contact.contact_dict.items():
                if contact_detail.lower() == value.lower():
                    matching_contacts.append(contact)
                    break

        if matching_contacts:
            print("Matching contacts:")
            for index, contact in enumerate(matching_contacts, 1):  
                print(f"{index} - {contact.contact_dict}")
        
        else:
            print("No contacts found matching the criteria.")


        while True:
            choice = input("Please select the contact number whose you want to delete ")
            if choice.isnumeric():
                choice = int(choice)
                if 1 <= choice <= len(matching_contacts):
                    selected_contact = matching_contacts[choice - 1]
                    self.contacts.remove(selected_contact)
                    deleted_contacts.append(selected_contact)
                    print(f"Contact deleted successfully.")
                    break
                            
                else:
                    print("Invalid value. Please try again.")
            else:
                print("Invalid input. Please enter a number.")
