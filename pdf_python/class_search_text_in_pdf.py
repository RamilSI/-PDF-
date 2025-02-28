# програмка извлечения текста из пдф-файла
# с помощью регулярных выражений вытаскиваю будущее имя файла


import re
import pymupdf


class NewNamePDF:

    def __init__(self, filename='/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan'):
        pdf_document = pymupdf.open(self.filename)
        print(pdf_document)
        text = ''
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]
            if page.get_text() != '':
                text += page.get_text()
                print('на странице есть текст: ', text)
            else:
                print('текста нет на странице')

        pdf_document.close()

        match1 = re.findall(r'Партия\s№\s[0-9]+', text)
        print(match1)
