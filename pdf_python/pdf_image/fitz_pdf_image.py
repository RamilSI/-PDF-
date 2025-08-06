import fitz
from datetime import datetime as dt

file = 'pdf_python/pdf_image/input_files/9_test_1.pdf'



# реальный код работающий

pdf_document = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/Сертификаты по дням ' \
               'прихода/08.04.24 — копия/6390 .pdf'
doc = fitz.open(pdf_document)
print('Исходный документ', doc)
print('\nКоличество страниц: %i\n\n-------------\n\n'% doc.page_count)
print(doc.metadata)
page_count = 0
for i in range(len(doc)):
    print('number of pages',i)
    for img in doc.get_page_images(i):
        xref = img[i]
        print('это хреф= ', xref)
        pix = fitz.Pixmap(doc, xref)
        pix1 = fitz.Pixmap(fitz.csRGB, pix)
        page_count +=1
        pix1.save('image/'+str(xref)+str(page_count) + str(i+1) +'.png')




now = dt.now()
print(now)