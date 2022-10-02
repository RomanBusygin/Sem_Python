import pytube, ui

url = ui.input_data('Введите ссылку на видео: ')
yt = pytube.YouTube(url)

mod = int(ui.input_data('Что сделать?\n1 - скачать видео\n2 - скачать аудио\n'))
match mod:
    case 1:
        yt.streams.get_by_resolution('720p').download()
    case 2:
        yt.streams.get_by_itag(140).download()