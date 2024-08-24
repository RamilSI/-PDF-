"""
1. передаю путь к целевой папке
2. сохраняю список файлов
3. создаю переменную для сохранения текста
4. проверяю название файла на не равенcтво . DC_Store
5. извлекаю весь текст файла
6. по шаблону '№\s[0-9][0-9][0-9][0-9]' ищу нужное совпадение (записать проверку наличия)
7. переименовываю на новое название

программа обхода имен(файлов) в папке и внутри нее поиска значений
входные переменные:
direct - целевая папка где находятся файлы пдф
"""

import os
import re
import fitz


direct = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07.08.24/'
files = os.listdir(direct)
print(files)
for i, line in enumerate(files):
    print('Текущее название: ', line)
    if line != '.DS_Store':
        pdf_document = fitz.open(direct + line)
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            if page.get_text() != '':
                text += page.get_text()
                print('на странице есть текст: ')
            else:
                print('текста нет на странице')
        match = re.findall(r'№\s[0-9][0-9][0-9][0-9]', text)
        pdf_document.close()
        print(f'Список имен: {match}')
        print('Новое название: ', ' '.join(match))
        path_old = direct + line
        print('Старое название', path_old)
        path_new = direct + ' '.join(match) + '.pdf'
        print('Новое название', path_new)
        print('\n', f'------КОНЕЦ {i} страницы -------', '\n')
        try:
            os.rename(path_old, path_new)
        except FileNotFoundError:
            print("Ошибка: Файл не найден")
        except PermissionError:
            print("Нет доступа для переименования файла")




