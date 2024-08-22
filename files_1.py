# программа обхода имен(файлов) в папке и внутри нее
# импортирую нужные библиотеки
import os
import re
import fitz
import shutil


# direct_ = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024'
direct = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024'
# direct = input('дайте url:  ')

files = os.listdir(direct)[0:7]
print(files)

file_str = []
path = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/'
for line in files:
    print('Текущее название: ', line)
    if line != '.DS_Store':
        filename = fitz.open(path + line)
        pdf_document = fitz.open(filename)
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
        match1 = re.findall(r'Партия\s№\s[0-9]+', text)

        print('Новое название: ', ' '.join(match1[0:2]))
        file_str.append(match1)
        path_ishod = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/' + line
        print(path_ishod)
        path_itog = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/' + ' '.join(match1[0:2]) + '.pdf'
        print(path_itog)
        try:
            os.rename(path_ishod, path_itog)
        except FileNotFoundError:
            print("Ошибка: Файл не найден")
        except PermissionError:
            print("Нет доступа для переименования файла")

q = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/07 авг 2024 002.pdf'
w = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/07 авг 2024 002.pdf'



