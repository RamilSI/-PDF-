import img2pdf
import fitz
import re
#
# a4_page_size = [img2pdf.in_to_pt(8.3), img2pdf.in_to_pt(11.7)]
# layout_function = img2pdf.get_layout_fun(a4_page_size)  # Источник: https://egorovegor.ru/python-image-to-pdf-convert
#
# pdf = img2pdf.convert(
#     '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/30.07.24/4313 4314.jpg',
#     layout_fun=layout_function)
# with open('A4_dog.pdf', 'wb') as f:
#     f.write(pdf)

filename = fitz.open('../../../files_storage/A4_dog.pdf')
pdf_document = fitz.open(filename)
print(pdf_document)
text = ''
for page_num in range(pdf_document.page_count):
    page = pdf_document[page_num]
    text += page.get_text()
    print(text)
match1 = re.findall(r'Партия\s№\s[0-9]+', text)
pdf_document.close()
print('Новое название: ', ' '.join(match1[0:2]))
