import re


def get_contact_by_id(self, contact_id):
    for contact in self.contacts:
        if contact.id == contact_id:
            return contact
    return None

def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

def validate_phone_number(phone_number):
    phone_regex = r'^0\d{2}-\d{3}-\d{3}$'
    return re.match(phone_regex, phone_number)