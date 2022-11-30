import data_provider as data
import model

def button_click():
    while True:
        act = data.get_action()
        if act == 0:
            print(model.look())
        elif act == 1:
            new_entry = model.add_user()
            model.export(new_entry)
        elif act == 2:
            row = data.get_row_index()
            del_entry = model.del_user(row)
            model.export(del_entry)
        elif act == 3:
            row = data.get_row_index()
            column = data.get_column()
            new_value = data.get_new_val()
            df_edit = model.edit(row, column, new_value)
            model.export(df_edit)
        else:
            print('До встречи!')
            break