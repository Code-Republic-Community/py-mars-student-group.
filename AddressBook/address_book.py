import json
import contact
import vaildation_checkers
import file_handler


class Addressbook:
    def __init__(self):
        self.contacts = []

    def search_contact(self, searching_word: str):
        for cont in self.contacts:
            for key in cont.dict_form:
                if searching_word.lower() in cont.dict_form[key].lower():
                    print(cont.dict_form)
                    break
            else:
                print('Nothing was found!')

    def add_contact(self, filename):
        name = input('Enter a name: ')
        mid_name = input('Enter a middle name: ')
        surname = input('Enter a surname: ')
        telephone = input('Enter a telephone: ')
        mail = input('Enter a mail: ')
        address = input('Enter an address: ')
        url = input('Enter a url: ')

        if not vaildation_checkers.is_valid_name(name):
            return 'Invalid name!'

        if not vaildation_checkers.is_valid_name(surname):
            return 'Invalid surname!'

        if not vaildation_checkers.is_valid_name(mid_name):
            return 'Invalid middle name!'

        if not vaildation_checkers.is_valid_telephone(telephone):
            return 'Invalid telephone!'

        if not vaildation_checkers.is_valid_address(address):
            return 'Invalid address!'

        if not vaildation_checkers.is_valid_mail(mail):
            return 'Invalid mail!'

        if not vaildation_checkers.is_valid_url(url):
            return 'Invalid url!'

        cont = contact.Contact(name, mid_name, surname, telephone, mail, address, url)
        self.contacts.append(cont)
        file_handler.add_to_file(filename,cont.dict_form)
        file_handler.add_to_json_data(cont.dict_form)
        print('Contact added successfully!')

    def update_contact(self, filename):
        if len(self.contacts) == 0:
            print('Before update a contact you must create it.')
            return
        index = 0
        nm = input('Enter a contact name whose information you want to update: ')
        for cont in self.contacts:
            if nm.lower() == cont.dict_form['name'].lower():
                index = self.contacts.index(cont)
                break
        else:
            print('No contact was found with that name!')
            return

        field = input('Enter a field you want to update (ex. name,mid_name,surname,telephone,mail,address,url): ')
        updated_value = input('Enter an updated value: ')
        for i in self.contacts[index].dict_form.keys():
            if i == field.lower():
                self.contacts[index].dict_form[i] = updated_value
                for cont in self.contacts:
                    file_handler.add_to_json_data(cont.dict_form)
                    file_handler.add_to_file(filename,cont.dict_form)
                print('Updated successfully!')
                break
        else:
            print('No such field in contact.')

    def delete_contact(self, filename):
        if len(self.contacts) == 0:
            print('No contacts to delete')
            return
        index = 0
        nm = input('Enter a contact name you want to delete: ')
        for cont in self.contacts:
            if nm.lower() == cont.dict_form['name'].lower():
                del cont
                for cont in self.contacts:
                    file_handler.add_to_json_data(cont.dict_form)
                    file_handler.add_to_file(filename,cont.dict_form)
                print('Deleted successfully!')
                break
        else:
            print('No contact was found with that name!')
            return

