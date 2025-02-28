import os

path_to_remove = '/Users/admin/PycharmProjects/files/платежи_кайт/'


for i, el in enumerate(os.listdir(path_to_remove)):
    print(el)
    os.remove(path_to_remove + el)