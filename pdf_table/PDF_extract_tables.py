import camelot
import pdfplumber
import pandas as pd
# pdf_path = '/content/drive/MyDrive/прайс АК ЛКМ 20.07.2022 с отверд-1.pdf'
pdf_path = 'pdf_table/Прайс для дилеров по компонентам 09.06.22.pdf'

tables = camelot.read_pdf(pdf_path)

"""Просто прочитать PDF файл"""

# with open(pdf_path, 'rb') as file:
#   file1 = open(r'pdfText.txt', 'a+')
#   pdfminer.high_level.extract_text_to_fp(file,file1)
#   file1.close()
"""Просто прочитать PDF файл вариант 2"""
with pdfplumber.open(pdf_path) as pdf:
    for i in range(len(pdf.pages)):
        # Прочитать страницу i + 1 PDF-документа
        page = pdf.pages[i]

        # page.extract_text () функция читает текстовое содержимое, следующим шагом будет удаление номера нижней страницы документа.
        tables = page.extract_tables()
        for table in tables:
            # df = pd.DataFrame(table)
            # Первый столбец используется в качестве заголовка:
            df = pd.DataFrame(table[1:], columns=table[0], index=None)