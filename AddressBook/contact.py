class ContactDescriptor:
    """
    Descriptor class for Contact class
    """
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name not in instance.__dict__:
            raise AttributeError(f"'{owner.__name__}' object has no attribute '{self.name}'")
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Contact:
    """
    Class contains all the fields of contact information and dictionary form representation
    """
    name = ContactDescriptor()
    surname = ContactDescriptor()
    mid_name = ContactDescriptor()
    telephone = ContactDescriptor()
    mail = ContactDescriptor()
    address = ContactDescriptor()
    url = ContactDescriptor()
    def __init__(self, name, mid_name, surname, telephone, mail, address, url):
        self.name = name
        self.mid_name = mid_name
        self.surname = surname
        self.telephone = telephone
        self.mail = mail
        self.address = address
        self.url = url
        self.dict_form = dict(name=self.name, mid_name=self.mid_name, surname=self.surname, telephone=self.telephone,
                              mail=self.mail, address=self.address, url=self.url)

