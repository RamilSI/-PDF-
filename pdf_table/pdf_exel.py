import tabula

pdf_path = 'pdf_table/прайс АК ЛКМ 20.07.2022 с отверд-1.pdf'
#
# dfs = tabula.read_pdf(pdf_path, pages='1', multiple_tables=True, encoding="utf-8")
# dfs[0].to_csv('page_1.csv')


dfs = tabula.read_pdf(pdf_path, pages='1',stream=False, encoding='utf-8', guess=True)
# read_pdf returns list of DataFrames
print(len(dfs))
print(dfs[0])
