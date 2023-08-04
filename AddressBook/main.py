from address_book import address_book
from address_book import contact
import os
from address_book import file_handler


def create_addressbook():
    filename = input('Enter a name for addressbook: ')
    print('Created successfully!')
    return address_book.Addressbook()


def delete_addressbook(filename):
    try:
        os.remove(f'{filename}.txt')
        print("Deleted successfully")
    except FileNotFoundError:
        print("File not found.")


def main():
    num = 0
    while True:
        print('\nHere are available options:')
        print('1 - Add contact\n2 - Update contact\n3 - Delete contact\n4 - Search '
              'contact\n5 - Create new addressbook\n6 - Delete addressbook\n7 - End program')

        opt = input('Please choose one of these option numbers: ')
        if opt == '1':
            cont = contact.Contact('name', 'mid name', 'surname', 'address', 'mail', 'telephone', 'url')
            filename = input('Enter addressbook name:')
            try:
                address_book.addressbook.add_contact(filename)
            except:
                print("Before adding contact you must create addressbook")
        elif opt == '2':
            try:
                address_book.addressbook.update_contact(filename)
            except:
                print('Before update a contact you must to create it.')

        elif opt == '3':
            filename = input('Enter addressbook name:')
            try:
                address_book.addressbook.delete_contact(filename)
            except:
                print('Before deleting a contact you must create addressbook and add contact')
        elif opt == '4':
            searching_word = input('Enter searching word: ')
            addressbook.search_contact(searching_word)
        elif opt == '5':
            addressbook = file_handler.create_addressbook()
        elif opt == '6':
            filename = input('Type the name of addressbook you want to delete: ')
            try:
                file_handler.delete_addressbook(filename)
            except ValueError:
                print('No such addressbook')

        elif opt == '7':
            break
        else:
            print('Please choose one of these numbers only, from 1 to 6! ')


if __name__ == '__main__':
    main()