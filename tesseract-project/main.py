import cv2
from PIL import Image
import re
import pytesseract

path_1 = '/Users/admin/PycharmProjects/files/платежи_кайт/3000 020924.PNG'
path_2 = '/Users/admin/PycharmProjects/files/платежи_кайт/3500 010924.PNG/'
path_3 = '/Users/admin/PycharmProjects/files/платежи_кайт/10000.PNG'
path_4 = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/2024-10-04 1.10.24 — jpg/1.10.24 018.jpg'

# img = cv2.imread('/Users/admin/Downloads/IMG_8108.PNG')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# config = r'--oem 3 --psm 6'
#
text_page = pytesseract.image_to_string(path_4, 'rus')
print(text_page)
# pattern = '[+][0-9]{11}|Сумма\s\d+.\d+|Получатель\s\w+'
pattern_1 = '№\s[0-9][0-9][0-9][0-9]'
match = re.findall(pattern_1, text_page)
# new_name = ''
# for i,el in enumerate(match):
#     new_name += el + '_'
#
# print(len(match))
# #
# match_1 = re.findall('[0-9]', match[0])
# match_2 = int(''.join(match_1))
print(match)
# print(match_2)


