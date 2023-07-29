from address_book.contact import Contact

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, keyword):
        result = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword.lower() in contact.surname.lower() or keyword in contact.phone_number or keyword.lower() in contact.email.lower() or keyword in contact.additional_info.values():
                result.append(contact)
        return result

    
    def update_contact(self, name, **kwargs):
        for contact in self.contacts:
            if contact.name == name:
                contact.update_contact(**kwargs)
                return True
        return False

    def delete_contact(self, contact_id):
        for contact in self.contacts:
            if contact.contact_id == contact_id:
                self.contacts.remove(contact)
                return True
        return False
    
    def get_all_contacts(self):
        return self.contacts

    def __str__(self):
        return "\n".join(str(contact) for contact in self.contacts)
