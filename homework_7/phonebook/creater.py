def export(text):
   with open('phonebook.csv', 'a', encoding='utf8') as f:
       print(text, file=f)
