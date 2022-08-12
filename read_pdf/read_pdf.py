from PyPDF2 import PdfFileReader

reader = PdfFileReader("WEGZINC 401.pdf", strict=True)
number_of_pages = reader.numPages
page = reader.pages[0]
text = page.extractText()
print(number_of_pages)