import ui, txt_format.ph_b_fun_txt as fun_txt, csv_format.ph_b_fun_csv as fun_csv


def phone_book():
    ui.out_data('В каком формате работаем?')
    ui.out_data('1 - csv')
    ui.out_data('2 - txt')
    format_file = int(ui.input_data(''))
    ui.out_data('Что хотите сделать?')
    ui.out_data('1 - Новая запись')
    ui.out_data('2 - Поиск по фамилии')
    ui.out_data('3 - Удалить запись (по фамилии)')
    ui.out_data('4 - Показать весь справочник')
    mod = int(ui.input_data(''))
    match format_file:
        case 1:
            match mod:
                case 1:
                    fun_csv.new_record_csv()
                case 2:
                    fun_csv.find_record_csv(ui.input_data('Кого ищем? '))
                case 3:
                    fun_csv.delete_record_csv(ui.input_data('Кого удалить? '))
                case 4:
                    fun_csv.all_records_csv()
        case 2:
            match mod:
                case 1:
                    fun_txt.new_record_txt()
                case 2:
                    fun_txt.find_record_txt(ui.input_data('Кого ищем? '))
                case 3:
                    fun_txt.delete_record_txt(ui.input_data('Кого удалить? '))
                case 4:
                    fun_txt.all_records_txt()