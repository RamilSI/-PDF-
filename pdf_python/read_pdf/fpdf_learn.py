from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

path1 = '/Users/admin/PycharmProjects/Константы/font/DejaVuSansCondensed.ttf'

pdf.add_font('DejaVu', '', path1, uni=True)
pdf.set_font('DejaVu', size=25)

pdf.cell(200, 10, txt='Изучение Питон', ln=1, align='C')

pdf.cell(200, 10, txt='Добро пожаловать на уроки изучения Питона', ln=1, align='L')

pdf.output('pdfTest.pdf')