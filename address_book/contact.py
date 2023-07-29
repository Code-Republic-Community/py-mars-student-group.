class Contact:
    def __init__(self, contact_id, name, surname, phone_number, email, additional_info=None):
        self.contact_id = contact_id
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.email = email
        self.additional_info = additional_info or {}

    def update_contact(self, phone_number=None, email=None, additional_info=None):
        if phone_number and self.validate_phone_number(phone_number):
            self.phone_number = phone_number
        elif phone_number:
            print("Invalid phone number format. Phone number not updated.")

        if email and self.validate_email(email):
            self.email = email
        elif email:
            print("Invalid email format. Email not updated.")

        if additional_info:
            self.additional_info.update(additional_info)

    def __str__(self):
        return f"ID: {self.contact_id}, Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}, Additional Info: {self.additional_info}"