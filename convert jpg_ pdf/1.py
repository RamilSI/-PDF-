import os
import PIL.Image


def img2pdf(fname):
    filename = fname
    name = filename.split('.')[0]
    im = PIL.Image.open(filename)
    if not os.path.exists('im2pdf_output'):
        os.makedirs('im2pdf_output')
    newfilename = ''.join(['im2pdf_output/', name, '.pdf'])
    PIL.Image.Image.save(im, newfilename, "PDF", resolution = 100.0)
    print("processed successfully: {}".format(newfilename))


files = [f for f in os.listdir('/Users/admin/PycharmProjects/file_meneger/files/Конвертер jpg в pdf пакетом/jpg_files_input') if f.endswith('.jpg')]
for fname in files:
    print(fname)
    img2pdf(fname)
