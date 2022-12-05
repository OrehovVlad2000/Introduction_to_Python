def get_name():
    name = input("Введите имя: ")
    return name

def get_surname():
    surname = input("Введите фамилию: ")
    return surname

def get_middle_name():
    middle_name = input("Введите отчество: ")
    return middle_name

def get_birthday():
    birt = input("Введите дату рождения: ")
    return birt

def get_phone():
    phone = input("Введите номер телефона: ")
    return phone

def get_job_title():
    job_title = input("Введите должность: ")
    return job_title

def get_action():
    return int(input('_________________________\n  0: Просмотр базы данных\n  1: Добавить запись\n '
                     ' 2: Удалить запись\n  3: Редактировать запись\n  4: Выход\nВыберите действие: '))

def get_row_index():
    index = int(input('Введите индекс строки: '))
    return index

def get_column():
    return int(input('0: Фамилия\n 1: Имя\n 2: Отчество\n 3: Дата рождения\n '
                     '4: Номер телефона\n 5: Должность\n Выберите столбец: '))

def get_new_val():
    return input('Введите новое значение: ')