# класс файлов сертификатов с нужными именами
import os
import fitz
import re


class Sert:

    def name(self):  # вытащить нужные имена файлов из текста файла.пдф
        import re
        import fitz
        pdf_document = fitz.open(self.path)
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
        match1 = re.findall(r'Партия\s№\s[0-9]+', text)

        return match1


class Pathfile:
    import os

    def __init__(self, direction):
        self.direction = direction

    def path_itog(self):
        path_i = os.listdir(self.direction)
        return path_i


class NewFname:
    pass


if __name__ == '__main__':
    pattern = 'Партия\s№\s[0-9]+'
    direct = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/21.08.24/Партия № 3927 Партия № 4019.pdf'
    path_1 = Pathfile(direct)
    sert_1 = Sert(pattern, direct)
    print(path_1.path_itog())
    # print(sert_1.pattern, sert_1.name())
