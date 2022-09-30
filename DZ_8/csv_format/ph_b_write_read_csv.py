import csv

def write_data(data):
    with open(path_file, 'a', encoding = 'utf8', newline = '') as file:
        csv.writer(file, delimiter = ',').writerow(data)

def read_all_data():
    with open(path_file, 'r', encoding = 'utf8') as file:
        ph_b = csv.reader(file, delimiter = ',')
        ph_b_list = [i for i in ph_b]
        return ph_b_list

def delete_rec(data):
    with open(path_file, 'a', encoding = 'utf8', newline = '') as file:
        csv.writer(file, delimiter = ',').writerow(data)

def clear_phone_book():
    with open(path_file, 'w', encoding = 'utf8', newline = '') as file:
        file.truncate


path_file = r'C:\Users\Roman\Desktop\GEEK\Block_2\Phyton\DZ\DZ_8\csv_format\phone_book.csv'