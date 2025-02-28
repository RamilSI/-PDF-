import os
import PIL.Image


filename = '/Users/admin/PycharmProjects/file_meneger/files/Конвертер jpg в pdf пакетом/jpg_files_input/4.jpg'
name = filename.split('.')[0]
print(name)
im = PIL.Image.open(filename)
print(im)
if not os.path.exists('im2pdf_output'):
    os.makedirs('im2pdf_output')
newfilename = ''.join([name, 'im2pdf_output', '.pdf'])
print('новое имя файла: ', newfilename)
PIL.Image.Image.save(im, newfilename, "PDF", resolution = 100.0)
# print("processed successfully: {}".format(newfilename))


files = [f for f in os.listdir('/Users/admin/PycharmProjects/file_meneger/files/Конвертер jpg в pdf пакетом/'
                               'jpg_files_input') if f.endswith('.jpg')]
for fname in files:
    print(fname)

