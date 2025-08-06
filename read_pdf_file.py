import os
import shutil
import re
import fitz

path_file = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/2025-02-04/Цвет RAL 7035 № 7529 № 8010 № 6477 № 7566 (перетянутый) 2.pdf'


text = ''
pdf_document = fitz.open(path_file)
for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    if page.get_text() != '':
        text += page.get_text()
        print('на странице есть текст: ')
        # match = re.findall(r'№\s[0-9][0-9][0-9][0-9]', text)
        pdf_document.close()
        # print(f'Список имен: {match}')
        # print('Новое название: ', ' '.join(match))

print('\n', f'------КОНЕЦ {text} страницы -------', '\n')