import pandas as pd
import data_provider as data
import logger

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 320)

def add_user():
    logger.logging.info('Добавление строки')
    df = pd.read_csv('database.csv')
    df.loc[len(df.index)] = [
        data.get_surname(),
        data.get_name(),
        data.get_middle_name(),
        data.get_birthday(),
        data.get_phone(),
        data.get_job_title()
    ]
    return df

def look():
    logger.logging.info('Просмотр базы данных')
    df = pd.read_csv('database.csv')
    return df

def del_user(row):
    logger.logging.info('Удаление строки')
    df = pd.read_csv('database.csv')
    df.drop([row], inplace=True)
    return df

def edit(row, col, val):
    logger.logging.info('Редактирование данных')
    col_list = ['Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Номер телефона', 'Должность']
    df = pd.read_csv('database.csv')
    df.loc[row, col_list[col]] = val
    return df

def export(new_data):
    logger.logging.info('Сохранение в файл')
    df = pd.DataFrame(new_data)
    df.to_csv('database.csv', index=False)