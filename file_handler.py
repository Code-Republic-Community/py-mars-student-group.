
def save_to_file(address_book, filename):
    data = {
        "Contacts": [contact.contact_dict for contact in address_book.contacts]
    }
    with open(filename, "w") as file:
        json.dump(data, file)
    print(f"Address book saved to {filename} successfully")


def load_from_file(address_book, filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            contacts_data = data.get("Contacts", [])
            address_book.contacts = [Contact(**contact_data) for contact_data in contacts_data]
            print("Address book loaded successfully.")
    except FileNotFoundError:
        print("File not found. Unable to load address book.")
    except Exception as e:
        print(f"Error occurred while loading the address book: {e}")
