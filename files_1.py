# программа обхода имен(файлов) в папке и внутри нее
# импортирую нужные библиотеки
"""
входные переменные:
1. direct - целевая папка где находятся файлы пдф
2.
"""




import os
import re
import fitz


direct = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/2024-06-18 +/'
files = os.listdir(direct)
print(files)

file_str = []
for i, line in enumerate(files):
    print('Текущее название: ', line)
    if line != '.DS_Store':
        filename = fitz.open(direct + line)
        pdf_document = fitz.open(filename)
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        match1 = re.findall(r'Партия\s№\s[0-9]+', text)
        match2 = re.findall(r'№\s[0-9][0-9][0-9][0-9]', text)
        pdf_document.close()
        print('Новое название: ', ' '.join(match2[0:2]))
        file_str.append(match2)
        path_old = direct + line
        print('Старое название', path_old)
        path_new = direct + ' '.join(match2[0:2]) + '.pdf'
        print('Новое название', path_old)
        print('\n', f'------КОНЕЦ {i} страницы -------', '\n')
        try:
            os.rename(path_old, path_new)
        except FileNotFoundError:
            print("Ошибка: Файл не найден")
        except PermissionError:
            print("Нет доступа для переименования файла")

q = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/07 авг 2024 002.pdf'
w = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07 авг 2024/07 авг 2024 002.pdf'



