from .contact import Contact
from typing import Dict, Callable, Any, Union
from .utils import valid_name, valid_email, valid_tel_number, valid_birthday, \
    convert_date_format


class AddressBook:
    """
        The AddressBook class represents a simple address book application.
        The address book stores a dictionary of contacts, where each contact is represented by the Contact class.

        Attributes:
            contacts (Dict[str, Contact]): A dictionary containing the Contact objects, where the keys are the telephone
                                           numbers of the contacts.

        Methods:
            add_contact(): Adds a new contact to the address book based on user input.
            search_contact(): Searches for a contact based on the user's search criteria (name, telephone number,
                              email, or birthday).
            delete_contact(): Deletes a contact from the address book based on the user's input (telephone number
                              or email address).
            update_contact(): Updates a contact's name, telephone number, or email address based on the user's input.
    """

    def __init__(self):
        self.contacts: Dict[str, Contact] = {}

    def add_contact(self) -> None:
        """
        Adds a new contact to the address book based on user input.
        """
        first_name = self._get_valid_input("Enter your first name: ", valid_name)
        middle_name = self._get_valid_input("Enter your middle name (optional): ", valid_name)
        last_name = self._get_valid_input("Enter your last name: ", valid_name)
        birthday = self._get_valid_input("Enter your birthday in the format DD.MM.YY (e.g.,01.01.20): ", valid_birthday)

        while True:
            tel_number = self._get_valid_input("Enter your telephone number in the format "
                                               "091XXXXXX or 374XXXXXXXX : ", valid_tel_number)
            if tel_number in self.contacts.keys():
                print("The telephone number already exists.")
                continue
            break
        while True:
            email = self._get_valid_input("Enter your email address: ", valid_email)
            if email.lower() in (c.email.lower() for c in self.contacts.values()):
                print("The email address already exists.")
                continue
            break
        contact = Contact(first_name, middle_name, last_name, birthday, tel_number, email)
        self.contacts[contact.tel_number] = contact
        print("Contact was added successfully!")

    @staticmethod
    def _get_valid_input(prompt: str, validator_func: Callable[[str], Union[str, bool]]) -> Union[str, None]:
        """
        Helper function to get and validate user input based on the provided validator function.
        """
        while True:
            user_input = input(prompt).strip()
            if prompt == "Enter your middle name (optional): " and user_input == "":
                return ""
            validated_input = validator_func(user_input)
            if validated_input:
                return validated_input
            else:
                print("Invalid input.")
                continue

    def search_contact(self) -> None:
        """
        Searches for a contact based on the user's search criteria (name, telephone number, email, or birthday).
        """
        while True:
            criteria = input("Enter search criteria: 1 for name, 2 for telephone number, 3 for email,"
                             " 4 for birthday, 0 to exit: ").strip()
            if criteria == "0":
                break
            elif criteria == "1":
                self.search_by_attribute("name", lambda contact: contact.first_name.lower() +
                                                                 ' ' + contact.middle_name.lower() +
                                                                 ' ' + contact.last_name.lower())
            elif criteria == "2":
                self.search_by_telephone_number()
            elif criteria == "3":
                self.search_by_attribute("email", lambda contact: contact.email.lower())
            elif criteria == "4":
                self.search_by_attribute("birthday", lambda contact: contact.birthday.lower())
            else:
                print("Invalid search criteria. Please enter a valid option.")

    def search_by_attribute(self, attribute_name: str, attribute_getter: Callable[[Contact], Any]) -> None:
        """
        Searches for a contact by the specified attribute.
        Parameters:
           attribute_name (str): The name of the attribute being searched (e.g., "name", "email").
           attribute_getter (Callable[[Contact], Any]): A function to extract the attribute value from a Contact object.
        """
        searched_value = input(f"Enter {attribute_name} of the contact you are looking for: ").strip().lower()
        if attribute_name == "birthday":
            try:
                searched_value = convert_date_format(searched_value).lower()
            except ValueError:
                print("Invalid input! Please enter a date in the correct format: DD.MM.YY (e.g., 01.12.20).")
        matching_contacts = [contact for contact in self.contacts.values()
                                 if searched_value in attribute_getter(contact)]
        if not matching_contacts:
            print(f"There is no contact with the {attribute_name} '{searched_value}' in the contacts.")
        else:
            print("Search results are:\n")
            for contact in matching_contacts:
                print(
                    f"name: {(contact.first_name + ' ' + contact.middle_name + ' ' + contact.last_name)}, "
                    f"birthday: {contact.birthday}, telephone number: {contact.tel_number}, email: {contact.email}\n")

    def search_by_telephone_number(self) -> None:
        """
        Searches for a contact by telephone number.
        """
        number = input("Enter tel number: ")
        number = number[0:3].replace("374", "0") + number[3:]
        matching_contacts = [contact for contact in self.contacts.values() if contact.tel_number.startswith(number)]
        if not matching_contacts:
            print("No matches.")
            return
        else:
            for contact in matching_contacts:
                print("Search results are:")
                print(
                    f"name: {(contact.first_name + ' ' + contact.middle_name + ' ' + contact.last_name)}, "
                    f"birthday: {contact.birthday}, telephone number: {contact.tel_number}, "
                    f"email: {contact.email}\n")

    def delete_contact(self) -> None:
        """
        Deletes a contact from the address book based on the user's input (telephone number or email address).
        """
        print("In order to delete a contact, you must enter either a telephone number or an email address.")
        contact = self.find_contact()
        if contact:
            warning = input("Are you sure about deleting the contact? Enter yes or no: ").strip().lower()
            if warning == "yes":
                self.contacts.pop(contact.tel_number)
                print("The contact was deleted successfully.")
            elif warning == "no":
                print("The contact is not deleted.")
            else:
                print("Invalid input! You must enter either 'yes' or 'no'.")

    def find_contact(self) -> Union[None, Contact]:
        criteria = input("Enter criteria: 1 for telephone number, 2 for email: ").strip()
        if criteria == "1":
            tel_number = self._get_valid_input("Enter telephone number of the contact you want to delete: ",
                                               valid_tel_number)
        elif criteria == "2":
            email = self._get_valid_input("Enter email address of the contact you want to delete: ", valid_email)
            contact = next((c for c in self.contacts.values() if c.email.lower() == email.lower()), None)
            tel_number = contact.tel_number if contact else None
        else:
            print("Invalid input! You must enter 1 or 2.")
            return
        if not tel_number:
            print("Contact not found.")
            return
        contact = self.contacts.get(tel_number)
        if not contact:
            print(f"There is no contact with {tel_number} telephone number.")
            return
        return contact

    def update_contact(self) -> None:
        """
        Updates a contact's name, birthday, telephone number or email address based on the user's input.
        """
        print("In order to update contact you must enter telephone number or email address: ")
        contact = self.find_contact()
        if contact:
            while True:
                criteria = input("Enter update criteria: 1 for first name, 2 for middle name, 3 for last name,"
                                 " 4 for telephone number, 5 for email, 6 for birthday, 0 to exit: ").strip()
                if criteria == "0":
                    break
                elif criteria == "1":
                    first_name = self._get_valid_input("Enter new first name: ", valid_name)
                    contact.first_name = first_name.title()
                elif criteria == "2":
                    middle_name = self._get_valid_input("Enter new middle name: ", valid_name)
                    contact.middle_name = middle_name.title() if middle_name else ""
                elif criteria == "3":
                    last_name = self._get_valid_input("Enter new last name: ", valid_name)
                    contact.last_name = last_name.title()
                elif criteria == "4":
                    tel_number = self._get_valid_input("Enter new telephone number: ", valid_tel_number)
                    if tel_number not in self.contacts.keys():
                        contact.tel_number = tel_number
                    else:
                        print("The telephone number already exists.")
                elif criteria == "5":
                    email = self._get_valid_input("Enter new email address: ", valid_email)
                    if email.lower() not in (c.email.lower() for c in self.contacts.values()):
                        contact.email = email
                    else:
                        print("The email address already exists.")
                elif criteria == "6":
                    birthday = self._get_valid_input("Enter new birthday in the format DD.MM.YY (e.g.,01.12.20): ",
                                                     valid_birthday)
                    contact.birthday = birthday
                else:
                    print("Invalid search criteria. Please enter a valid option.")
