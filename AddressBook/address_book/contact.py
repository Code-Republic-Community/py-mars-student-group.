import re


class Contact:
    def __init__(self):
        while True:
            self.first_name = input("Enter your first name: ").capitalize()
            if self.valid_name(self.first_name):
                break
            continue
        while True:
            self.last_name = input("Enter your last name: ").capitalize()
            if self.valid_name(self.last_name):
                break
            continue
        while True:
            self.middle_name = input("Enter your middle name: ").capitalize()
            if self.middle_name:
                if self.valid_name(self.last_name):
                    break
                continue
            break

    @staticmethod
    def valid_name(name):
        min_length = 2
        max_length = 50
        allowed_characters = r"^[A-Za-z -]+$"
        if len(name) < min_length or len(name) > max_length:
            return False
        if not re.match(allowed_characters, name):
            return False
        return True


