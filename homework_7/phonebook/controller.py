import data_provider as data
import model
import creater

def button_click():
    while True:
        act = data.get_action()
        if act == 0:
            print(model.look())
        elif act == 1:
            name = data.get_name()
            surname = data.get_surname()
            birthday = data.get_birthday()
            phone = data.get_phone()
            text = model.add_user(name, surname, birthday, phone)
            creater.export(text)
        else:
            print('До встречи!')
            break
