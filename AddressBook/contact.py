class Contact:
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

