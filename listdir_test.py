import os
import re
path = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/База сертификатов'

# удалить не нужный файл: find . -name ".DS_Store" -delete
print(os.listdir(path))

for i, name in enumerate(os.listdir(path)):
   print(i, name)