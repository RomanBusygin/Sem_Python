def write_data(data):
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_7\phone_book.txt', 'a', encoding = 'utf8') as file:
        file.write(f'{data}\n')

def read_all_data():
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_7\phone_book.txt', 'r', encoding = 'utf8') as file:
        return file.readlines()

def delete_rec(data):
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_7\phone_book.txt', 'a', encoding = 'utf8') as file:
        file.write(f'{data}')

def clear_phone_book():
    with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_7\phone_book.txt', 'w', encoding = 'utf8') as file:
        file.write('')