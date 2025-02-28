
import pdfplumber
import pandas as pd
pdf_path = '../../../files_storage/прайс АК ЛКМ 20.07.2022 с отверд-1.pdf'
pdf_path_11122 = '/Users/admin/new/Rem_Color/Прайсы Рем_Колор/прайс АК ЛКМ 22.08.2022 с отверд.pdf'



"""Просто прочитать PDF файл"""

# with open(pdf_path, 'rb') as file:
#   file1 = open(r'pdfText.txt', 'a+')
#   pdfminer.high_level.extract_text_to_fp(file,file1)
#   file1.close()
"""Просто прочитать PDF файл вариант 2"""
# with pdfplumber.open(pdf_path) as pdf:
#     for i in range(len(pdf.pages)):
#         # Прочитать страницу i + 1 PDF-документа
#         page = pdf.pages[i]
#
#         # page.extract_text () функция читает текстовое содержимое, следующим шагом будет удаление номера нижней страницы документа.
#         tables = page.extract_tables()
#         for table in tables:
#             # df = pd.DataFrame(table)
#             # Первый столбец используется в качестве заголовка:
#             df = pd.DataFrame(table[1:], columns=table[0], index=None)

# прочесть первую страницу таблицы и записать в df
with pdfplumber.open(pdf_path) as pdf:
    first_page = pdf.pages[0]
    tables = first_page.extract_tables()
    for table in tables:
        #df = pd.DataFrame(table)
                 # Первый столбец используется в качестве заголовка:
        df = pd.DataFrame(table[1:],columns=table[0], index=None)

name_col = df.columns

# прочесть вторую страницу таблицы и записать в df2
with pdfplumber.open(pdf_path) as pdf:
    second_page = pdf.pages[1]
    tables = second_page.extract_tables()
    for table in tables:
        #df = pd.DataFrame(table)
                 # Первый столбец используется в качестве заголовка:
        df2 = pd.DataFrame(table[1:],columns=table[0], index=None)

# оформление столбцов в df2
df2 = pd.concat([pd.DataFrame([df2.columns.values], columns=df2.columns), df2], ignore_index=True)

df2.columns = name_col

# Объединяет Оба дата фрейма
df = df.append(df2)

print(df.head())
df = df.set_index('№')

# df['НАИМЕНОВАНИЕ'].fillna(method='ffill', inplace=True)
df.fillna(method='ffill', inplace=True)

df['Name']=df['НАИМЕНОВАНИЕ'].str.split('\n').str.get(0)

df['Функция']= df['НАИМЕНОВАНИЕ'].str.split('\n').str.get(1) + df['НАИМЕНОВАНИЕ'].str.split('\n').str.get(2)

df.pop('НАИМЕНОВАНИЕ')
df = df.reindex(columns=['Name', 'Функция', 'ХАРАКТЕРИСТИКА МАТЕРИАЛА И ПОКРЫТИЯ','Цена* без НДС, \nевро/кг'])

df.to_csv('price_rem_color.csv')