import json


def add_to_file(filename, data):
    with open(f'{filename}.txt', 'a') as f:
        f.write(data)


def add_to_json_data(data):
    with open('address_book_data.json', 'a') as f:
        json.dump(data, f)
