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


class FileHandler:
    """ Работа с файловой системой """
    def __init__(self, root_path, dir_path):
        self.root_path = os.path.join(root_path, dir_path)
        self.files = self._get_filtered_files()
        print(self.files)

    def _get_filtered_files(self):
        """ Фильтр исключающий файл .DS_Store"""
        return [f for f in os.listdir(self.root_path) if f != '.DS_Store']


class PDFProcessor:
    """Обработка PDF-файлов"""
    def __init__(self, pattern):
        self.pattern = re.compile(pattern)

    def extract_text(self, file_path) -> list:
        """Извлекает текст из PDF"""
        with fitz.open(file_path) as doc:
            print(doc)
            return "".join(page.get_text for page in doc if page.get_text())

    def find_matches(self, text):
        """Ищет совпадения по паттерну"""
        return self.pattern.findall(text)


class FileRename:
    """Переименование и перемещение файлов"""
    @staticmethod
    def sanitize(name):
        return re.sub(r'[\\/*?:"|<>]', '_', name).strip(' .')

    def rename(self, src, dest_dir):
        """Безопасное переименование с обработкой ошибок"""
        try:
            shutil.move(src, dest_dir)
        except(FileNotFoundError, PermissionError) as e:
            print(f'Ошибка {e}')


config = {
    'root_path': '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/',
    'dir_path' : 'Новая папка/',
    'pattern' :  r'№\s[0-9][0-9][0-9][0-9]|Цвет\sRAL\s\d+|№\s\d+[/]\d+',
    'dest_dir' : '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/base_sert'
}


class SertificateProcessor:
    def __init__(self, config):
        self.file_handler = FileHandler(config['root_path'], config['dir_path'])
        self.pdf_processor = PDFProcessor(config['pattern'])
        self.rename = FileRename()
        self.dest_dir = config['dest_dir']

    def process_files(self):
        for file_name in self.file_handler.files:
            src_path = os.path.join(self.file_handler.root_path, file_name)
            print(f'старый путь: {src_path}')
        #     извлекаем тексте и ищем совпадения
            text = self.pdf_processor.extract_text(src_path)
            print(f' text {text}')
            matches = self.pdf_processor.find_matches(text)
            print(f' new name file: {matches}')

        #  формируем новое имя
            clean_name = self.sanitize_filename(' '.join(matches))
            dest_path = os.path.join(self.dest_dir, f'{clean_name}.pdf')

        #     переименование
            self.rename.rename(src_path, dest_path)


if __name__ == '__main__':

    processor = SertificateProcessor(config)
    processor.process_files()