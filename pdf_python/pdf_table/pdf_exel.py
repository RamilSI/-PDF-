import tabula


pdf_path = '/Users/admin/PycharmProjects/Image_story/pdf_python/pdf_image/input_files/прайс Тональ ФЕВРАЛЬ 2024.pdf'
#
# dfs = tabula.read_pdf(pdf_path, pages='1', multiple_tables=True, encoding="utf-8")
# dfs[0].to_csv('page_1.csv')


dfs = tabula.read_pdf(pdf_path, pages='1', stream=True, encoding='utf-8', guess=True)
# read_pdf returns list of DataFrames
print(len(dfs))
print(dfs[0])
