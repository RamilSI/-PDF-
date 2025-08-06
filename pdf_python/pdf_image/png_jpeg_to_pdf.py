# import os
# import PIL.Image
# from PIL import ImageFilter
# from PyPDF2 import PdfFileMerger

# УЛУЧШАЮ КАЧЕСТВО ИСХОДНИКОВ
# dir_path = 'input_files/test_png/'
# files = [f for f in os.listdir(dir_path) if f.endswith('.png')]
# for fname in files:
#     full_path = dir_path + fname
#     print(full_path)
#     image = PIL.Image.open(full_path)
#     blurred_jelly = image.filter(ImageFilter.SHARPEN)
#     blurred_jelly.save(full_path)

#
# # выведу дир-пасс в отдельную переменную
# def img2pdf(fname,dir_path,dir_out_path):
#     filename = fname
#     name = filename.split('.')[0]
#     im = PIL.Image.open(dir_path + filename)
#     if not os.path.exists(dir_out_path):
#         os.makedirs(dir_out_path)
#     newfilename = ''.join([dir_out_path,name,'.pdf'])
#     PIL.Image.Image.save(im, newfilename, "PDF", resolution = 200.0)
#     print("processed successfully: {}".format(newfilename))
#
# dir_out_path = 'output_files_pdf/'
# dir_path = 'input_files/test_png/'
#
# files = [f for f in os.listdir(dir_path) if f.endswith('.png')]
# for fname in files:
#     print(fname)
#     img2pdf(fname, dir_path,dir_out_path)



# merger = PdfFileMerger()
# merger.append('output_files_pdf/1str.pdf')
# merger.append('output_files_pdf/2str.pdf')
# merger.write('result.pdf')
# merger.close()

#
# dir_out_path = 'output_files_pdf/'
# merger = PdfFileMerger()
# for pdf in sorted(os.listdir(dir_out_path)):
#     print(dir_out_path+pdf)
#     merger.append(dir_out_path+pdf)
#
#
# merger.write(dir_out_path+"result.pdf")
# merger.close()



