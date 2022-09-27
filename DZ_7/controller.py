import ui, ph_b_fun as fun


def phone_book():
    ui.out_data('Что хотите сделать?')
    ui.out_data('1 - Новая запись')
    ui.out_data('2 - Поиск по фамилии')
    ui.out_data('3 - Удалить запись (по фамилии)')
    ui.out_data('4 - Показать весь справочник')
    mod = int(ui.input_data(''))
    ui.out_data
    match mod:
        case 1:
            fun.add_record()
        case 2:
            fun.find_record(ui.input_data('Кого ищем? '))
        case 3:
            fun.delete_record(ui.input_data('Кого удалить? '))
        case 4:
            fun.all_records()