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
import os
import shutil
import re
import fitz


class Sert:

    def __init__(self, root_path='/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/',
                 dir_path='',
                 path_new='/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/base_sert',
                 pattern=r'№\s[0-9][0-9][0-9][0-9]|Цвет\sRAL\s\d+|№\s\d+[/]\d+'):  # паттерн регулярного выражения и пути к нужному файлу
        self.root_path = root_path
        self.dir_path = dir_path
        self.pattern = pattern
        self.path_new = path_new
        self.__direct = root_path + dir_path
        self.files = os.listdir(root_path + dir_path)
        for i, name in enumerate(os.listdir(self.__direct)):
            print(i, name)
        print("список файлов: ", os.listdir(self.root_path + self.dir_path))
        print('длина списка', len(self.files))

    def sanitize_filename(self, name):
        # Заменяем запрещённые символы на подчёркивания
        cleaned = re.sub(r'[\\/*?:"<>|]', '_', name)
        # Удаляем начальные/конечные пробелы и точки
        cleaned = cleaned.strip(' .')
        # Заменяем множественные пробелы на один
        cleaned = re.sub(r'\s+', ' ', cleaned)
        return cleaned

    def new_name(self):
        for i, line in enumerate(os.listdir(self.__direct)):
            if line != '.DS_Store':
                pdf_document = fitz.open(self.__direct + line)
                text = ''
                for page_num in range(pdf_document.page_count):
                    page = pdf_document[page_num]
                    if page.get_text() != '':
                        text += page.get_text()
                    else:
                        print('текста нет на странице')
                match = re.findall(self.pattern, text)
                pdf_document.close()
                path_old = os.path.join(self.__direct, line)
                # path_old = self.__direct + line
                print('Старое название', path_old)

                # В методе new_name измените формирование path_new:
                match_str = ' '.join(match)
                cleaned_name = self.sanitize_filename(match_str)
                path_new = os.path.join(self.__direct, f"{cleaned_name}.pdf")

                # path_new = self.__direct + ' '.join(match) + '.pdf'
                print('Новое название', path_new)
                print('\n', f'------КОНЕЦ {i} страницы -------', '\n')

                try:
                    os.rename(path_old, path_new)
                    print(self.files)
                except FileNotFoundError:
                    print("Ошибка: Файл не найден")
                except PermissionError:
                    print("Нет доступа для переименования файла")

    def new_root(self):
        for i, file in enumerate(os.listdir(self.__direct)):
            if file != '.DS_Store':
                path_current = self.root_path + self.dir_path + file
                if file not in (os.listdir(self.path_new)):
                    print(f'номер строки: {i} - файл - {file}')
                    shutil.move(path_current, self.path_new)
                else:
                    print('файл уже присутствует!', file)
            else:
                print(file)
                os.remove(self.root_path+self.dir_path+file)

        os.rmdir(self.root_path + self.dir_path)


if __name__ == '__main__':

    sert_1 = Sert(dir_path='new/')
    sert_1.new_name()
    sert_1.new_root()
