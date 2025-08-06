import os

path = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/19.07.24 копия'
spisok = os.listdir(path)

for i in spisok:
    print(i)

print(len(spisok))