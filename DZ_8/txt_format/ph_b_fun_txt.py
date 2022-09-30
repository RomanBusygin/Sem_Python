import ui, txt_format.ph_b_write_read_txt as wr


def new_record_txt():
    sec_name = ui.input_data('Введите фамилию: ')
    first_name = ui.input_data('Введите имя: ')
    phone = ui.input_data('Введите телефон: ')
    wr.write_data(f'{sec_name}. {first_name}. {phone}')

def find_record_txt(sec_name):
    ph_b = wr.read_all_data()
    for i in range(len(ph_b)):
        if sec_name in ph_b[i]:
            print(ph_b[i], end = '')

def delete_record_txt(sec_name):
    ph_b = wr.read_all_data()
    wr.clear_phone_book()
    for i in ph_b:
        if sec_name not in i:
            wr.delete_rec(i)

def all_records_txt():
    ph_b = wr.read_all_data()
    for i in ph_b:
        print(i, end = '')