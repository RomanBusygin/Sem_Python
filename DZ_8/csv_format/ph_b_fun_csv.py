import ui, csv_format.ph_b_write_read_csv as wr


def new_record_csv():
    sec_name = ui.input_data('Введите фамилию: ')
    first_name = ui.input_data('Введите имя: ')
    phone = ui.input_data('Введите телефон: ')
    csv_list = [sec_name, first_name, phone]
    wr.write_data(csv_list)

def find_record_csv(sec_name):
    ph_b = wr.read_all_data()
    for i in range(len(ph_b)):
        if sec_name in ph_b[i]:
            for j in range(len(ph_b[i])):
                print(ph_b[i][j], end = ' ')

def delete_record_csv(sec_name):
    ph_b = wr.read_all_data()
    wr.clear_phone_book()
    for i in ph_b:
        if sec_name not in i:
            wr.delete_rec(i)

def all_records_csv():
    ph_b = wr.read_all_data()
    for i in range(len(ph_b)):
        print('')
        for j in range(len(ph_b[i])):
            print(f'{ph_b[i][j]}', end = ' ')