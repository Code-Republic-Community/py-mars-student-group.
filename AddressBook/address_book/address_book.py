from datetime import datetime
from re import match
from .contact import Contact
from typing import List


class AddressBook:
    def __init__(self):
        self.contacts: List[Contact] = []

    def add_contact(self) -> None:
        while True:
            first_name = input("Enter your first name: ").title()
            if self.valid_name(first_name):
                break
            print("This field can't be empty and must include only letters at least two and '-'.")
            continue
        while True:
            last_name = input("Enter your last name: ").capitalize()
            if self.valid_name(last_name):
                break
            print("This field can't be empty and must include only letters at least two and '-'.")
            continue
        while True:
            middle_name = input("Enter your middle name: ").capitalize()
            if middle_name:
                if self.valid_name(middle_name):
                    break
                print("This field can be empty or must include only letters at least two and '-'.")
                continue
            break
        while True:
            try:
                input_date = input("Enter a date in the format DD.MM.YY (e.g., 01.12.20): ")
                birthday = self.convert_date_format(input_date)
            except ValueError:
                print("Invalid input! Please enter a date in the correct format.")
                continue
            else:
                break
        while True:
            tel_number = input("Enter your telephone number: ").replace(" ", "").replace("-", "")
            if self.valid_tel_number(tel_number):
                if len(tel_number) == 11 and tel_number[0:3] == "374":
                    tel_number = tel_number[0:3].replace("374", "0") + tel_number[3:]
                else:
                    if tel_number in (c.tel_number for c in self.contacts):
                        print("The telephone number already exists, try another one.")
                        continue
                    break
            else:
                print("Invalid telephone number.")
                continue
        while True:
            email = input("Enter your email address: ")
            if self.valid_email(email):
                if email.lower() in (c.email.lower() for c in self.contacts):
                    print("The email address already exists, try another one.")
                    continue
                break
            print("Invalid email.")
            continue
        my_contact = Contact(first_name, middle_name, last_name, birthday, tel_number, email)
        self.contacts.append(my_contact)
        print("Contact was successfully added.")

    def search_contact(self) -> None:
        while True:
            criteria = input("Enter search criteria: 1 for name, 2 for telephone_number, 3 for email, 4 for birthday,"
                             " 0 to exit: ")
            if "1" == criteria.strip():
                searched_name = input("Enter name of the contact you are looking for: ")
                if all(searched_name.lower() not in contact_name for contact_name in (c.name.lower() for c in self.contacts)):
                    print(f"There is no contact with {searched_name} name in the contacts.")
                else:
                    print("Possible matches are as below:\n")
                    for contact in self.contacts:
                        if searched_name.lower() in contact.name.lower():
                            print(f"name: {contact.name}, birthday: {contact.birthday}, telephone number: {contact.tel_number}, email: {contact.email}\n")
            if "2" == criteria.strip():
                ordinals = {
                    1: "first", 2: "second", 3: "third", 4: "fourth",
                    5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth",
                    9: "ninth"
                }
                number = ""
                loop_count = 1
                while True:
                    digit = input(f"Enter {ordinals[loop_count]} digit of telephone number you are looking for: ")
                    if not digit.strip().isdigit() or len(digit) > 1:
                        print("Enter one digit.")
                        continue
                    number += digit
                    if all(not tel_number.startswith(number) for tel_number in (c.tel_number for c in self.contacts)):
                        print("No matches.")
                        return
                    else:
                        for contact in self.contacts:
                            if contact.tel_number.startswith(number):
                                if loop_count < 9:
                                    print(f"Possible match: {contact.tel_number[:loop_count]}{(9-loop_count)*'X'}\n")
                                if loop_count == 9:
                                    print("Search results are:")
                                    print(f"name: {contact.name}, birthday: {contact.birthday}, telephone number: {contact.tel_number}, email: {contact.email}\n")
                        loop_count += 1
                        if len(number) == 9:
                            return
            if "3" == criteria.strip():
                searched_email = input("Enter email address of the contact you are looking for: ")
                if all(searched_email.lower() not in (c.email.lower() for c in self.contacts)):
                    print(f"There is no contact with {searched_email} email in the contacts.")
                else:
                    print("Search results are:\n")
                    for contact in self.contacts:
                        if searched_email.lower() in contact.email.lower():
                            print(f"name: {contact.name}, birthday: {contact.birthday}, telephone number: {contact.tel_number}, email: {contact.email}\n")
            if "4" == criteria.strip():
                while True:
                    try:
                        input_date = input("Enter birthday of the contact you are looking for in the format DD.MM.YY"
                                           " (e.g., 01.12.20): ")
                        searched_birthday = self.convert_date_format(input_date)
                    except ValueError:
                        print("Invalid input! Please enter a date in the correct format.")
                        continue
                    else:
                        break
                if all(searched_birthday != birthday for birthday in (c.birthday for c in self.contacts)):
                    print(f"There is no contact with {searched_birthday} birthday in the contacts.")
                else:
                    print("Search results are:\n")
                    for contact in self.contacts:
                        if searched_birthday == contact.birthday:
                            print(f"name: {contact.name}, birthday: {contact.birthday}, telephone number: {contact.tel_number}, email: {contact.email}\n")
            if "0" in criteria:
                break

    def delete_contact(self) -> None:
        print("In order to delete contact you must enter either telephone number or email address: ")
        criteria = input("Enter criteria: 1 for telephone_number, 2 for email.")
        if "1" == criteria.strip():
            tel_number = input("Enter telephone number of the contact you want to delete: ")
            if not self.valid_tel_number(tel_number):
                print("Invalid tel number.")
            else:
                if tel_number not in (c.tel_number for c in self.contacts):
                    print(f"There is no contact with {tel_number} telephone number. ")
                    return
                contact = next((c for c in self.contacts if c.tel_number == tel_number))
                warning = input("Are you sure about deleting the contact? Enter yes or no: ")
                if warning.strip().lower() == "yes":
                    self.contacts.remove(contact)
                    print("The contact is deleted successfully.")
                if warning.strip().lower() == "no":
                    print("The contact is not deleted.'")
        if "2" == criteria.strip():
            email = input("Enter email address of the contact you want to delete: ")
            if not self.valid_email(email):
                print("Invalid email address.")
            else:
                if email not in (c.email for c in self.contacts):
                    print(f"There is no contact with {email} email address. ")
                    return
                contact = next((c for c in self.contacts if c.email == email))
                warning = input("Are you sure about deleting the contact? Enter yes or no: ")
                if warning.strip().lower() == "yes":
                    self.contacts.remove(contact)
                    print("The contact was deleted successfully.")
                if warning.strip().lower() == "no":
                    print("The contact is not deleted.'")

    def update_contact(self) -> None:
        print("In order to update contact you must enter telephone number or email address: ")
        criteria = input("Enter criteria: 1 for telephone_number, 2 for email.")
        if "1" == criteria.strip():
            tel_number = input("Enter telephone number you want to change: ")
            if not self.valid_tel_number(tel_number):
                print("Invalid telephone number.")
            else:
                if tel_number not in (c.tel_number for c in self.contacts):
                    print(f"There is no contact with {tel_number} telephone number. ")
                    return
                contact = next((c for c in self.contacts if c.tel_number == tel_number))
                while True:
                    tel_number = input("Enter new telephone number: ").replace(" ", "").replace("-", "")
                    if self.valid_tel_number(tel_number) and tel_number not in (c.tel_number for c in self.contacts):
                        warning = input("Are you sure about changing the telephone number? Enter yes or no: ")
                        if warning.strip().lower() == "yes":
                            if len(tel_number) == 11 and tel_number[0:3] == "374":
                                contact.tel_number = tel_number[0:3].replace("374", "0") + tel_number[3:]
                                print("The contact was updated successfully.")
                                break
                            contact.tel_number = tel_number
                            print("The contact was updated successfully.")
                            break
                        if warning.strip().lower() == "no":
                            print("The contact is not changed.")
                            break
                        else:
                            print("Unacceptable answer.")
                            break
                    print("Invalid or existing telephone number.")
                    continue
        elif "2" == criteria.strip():
            email = input("Enter email address of the contact you want to change: ")
            if not self.valid_email(email):
                print("Invalid email address.")
            else:
                if email not in (c.email for c in self.contacts):
                    print(f"There is no contact with {email} email address. ")
                    return
                contact = next((c for c in self.contacts if c.email == email))
                while True:
                    email = input("Enter new email address: ")
                    if self.valid_email(email) and email not in (c.email for c in self.contacts):
                        warning = input("Are you sure about changing the email address? Enter yes or no: ")
                        if warning.strip().lower() == "yes":
                            contact.email = email
                            print("The contact was updated successfully.")
                            break
                        if warning.strip().lower() == "no":
                            print("The contact is not changed.")
                            break
                        else:
                            print("Unacceptable answer.")
                            break
                    print("Invalid or existing email.")
                    continue
        else:
            print("You must enter one number from the list.")

    @staticmethod
    def valid_tel_number(tel_number: str) -> bool:
        valid_oper = ["93", "94", "98", "91", "43", "11"]
        if tel_number.isdigit() and (tel_number[0] == "0" and tel_number[1:3] in valid_oper and len(tel_number[3:]) == 6) or \
                (tel_number[0:3] == "374" and tel_number[3:5] in valid_oper and len(tel_number[5:]) == 6):
            return True
        return False

    @staticmethod
    def valid_email(email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return match(pattern, email) is not None

    @staticmethod
    def valid_name(name: str) -> bool:
        min_length = 2
        max_length = 50
        allowed_characters = r"^[A-Za-z -]+$"
        if len(name) < min_length or len(name) > max_length:
            return False
        if not match(allowed_characters, name):
            return False
        return True

    @staticmethod
    def convert_date_format(input_date: str) -> str:
        date = datetime.strptime(input_date, "%d.%m.%y")
        if int(str(date.year)[-2:]) > int(str(datetime.now().year)[-2:]):
            date = date.replace(year=date.year - 100)
        result = date.strftime("%d.%b.%Y")
        return result

