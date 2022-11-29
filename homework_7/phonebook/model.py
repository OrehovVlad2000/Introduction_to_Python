def add_user(name, surname, birt, phone):
    text = f'{name} {surname} {birt} {phone}'
    return text

def look():
    with open('phonebook.csv', 'r', encoding='utf8') as f:
        return f.read()
