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
import pytesseract

pattern = '[+][0-9]{11}|Сумма\s\d+.\d+|Получатель\s\w+'
pattern_1 = '\d{2}\s[а-я]+|[0-9]{4}Р|\d+\D\w+Р'
pattern_2 = '\d{2}\s[а-я]+|\s[0-9]{4}[Рр]|\d+\D\w+Р'
pattern_3 = '№\s[0-9][0-9][0-9][0-9]'


direct = '/Users/admin/PycharmProjects/files/платежи_кайт/'
direct_1 = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/2024-10-04 1.10.24 —' \
           ' jpg_копия'
files = os.listdir(direct_1)
# print(files)
summa = []
for el in files:
    print('Текущее название: ', el)
    png_document = pytesseract.image_to_string(direct_1 + el, 'rus')
    match = re.findall(pattern_3, png_document)
    print(match)
    new_name = ''
    if len(match) > 1:
        for elem in match:
            new_name += elem + '_'
            match_1 = re.findall('[0-9]', match[1])
            match_2 = int(''.join(match_1))
        # summa.append(match_2)

        print(f'Новое название файла: {new_name}')
        # print(f'сумма платежа: {match_2}')
    else:
        match_1 = re.findall('[0-9]', match[0])
        match_2 = int(''.join(match_1))
        print(f'Перевод на карту: {match_2}')
        # summa.append(match_2)

    # print('сумма перевода на телефон: ', summa)

    path_old = direct_1 + el
    print('path_old: ', path_old)
    path_new = direct_1 + new_name + '.jpg'
    print('path_new: ', path_new)
    try:
        os.rename(path_old, path_new)
    except FileNotFoundError:
        print("Ошибка: Файл не найден")
    except PermissionError:
        print("Нет доступа для переименования файла")





