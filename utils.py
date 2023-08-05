from address_book import AddressBook
from main import address_books
def create_address_book():
    name = input("Enter the name for the new address book: ")
    address_book = AddressBook(name)
    address_books.append(address_book)
    print(f"Address book '{name}' created successfully!")


def choose_address_book():
    print("Choose an address book")
    for index, address_book in enumerate(address_books, 1):
        print(f"{index} - {address_book.name}")

    choice = input("Enter the number of the address book you want to use: ")
    try:
        choice = int(choice)
        if 1<= choice <=len(address_books):
            return address_books[choice - 1]
        else:
            print("Invalid choice. Using the first address book.")
            return address_books[0]
        
    except ValueError:
        print("Invalid input. Using the first address book.")
        return address_books[0]
    
