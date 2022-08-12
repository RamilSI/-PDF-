import pdfminer.high_level

with open('WEGZINC 401.pdf', 'rb') as file:
    file_1 = open(r'pdfText.txt', 'a+')

    pdfminer.high_level.extract_text_to_fp(file, file_1)
    file_1.close()



