"""
перевожу код на ООП
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


class Sert:

    def __init__(self, patern, direct):  # инициализирую паттерн регулярного выражения и пути к нужному файлу
        self.direct = direct
        self.patern = patern

    def new_name(self):
        import re
        import fitz
        import os
        for i, line in enumerate(os.listdir(self.direct)):
            if line != '.DS_Store':
                pdf_document = fitz.open(direct + line)
                text = ''
                for page_num in range(pdf_document.page_count):
                    page = pdf_document[page_num]
                    if page.get_text() != '':
                        text += page.get_text()
                    else:
                        print('текста нет на странице')
                match = re.findall(r'№\s[0-9][0-9][0-9][0-9]', text)
                pdf_document.close()
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

    def list_sert(self):
        import os
        for i, name in enumerate(os.listdir(self.direct)):
            print(i, name)


if __name__ == '__main__':
    pattern = 'Партия\s№\s[0-9]+'
    direct = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/07.08.24/'
    sert_1 = Sert(pattern, direct)

    sert_1.new_name()
    sert_1.list_sert()