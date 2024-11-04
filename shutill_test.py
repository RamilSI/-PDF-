import shutil
import os


class NewRoot:

    def __init__(self, root_path='/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/',
                 path_new='/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/scan/base_sert',
                 dir_path=''):
        self.root_path = root_path
        self.path_new = path_new
        self.dir_path = dir_path
        _direct = self.root_path + self.dir_path
        for i, file in enumerate(os.listdir(_direct)):
            if file != '.DS_Store':
                path_current = self.root_path + self.dir_path + file
                if file not in (os.listdir(path_new)):
                    print(f'номер строки: {i} - файл - {file}')
                    shutil.move(path_current, path_new)
                else:
                    print('файл уже присутствует!', file)
            else:
                print(file)
                os.remove(self.root_path + dir_path + file)

        try:
            os.rmdir(root_path + dir_path)
        except OSError:
            print("Нельзя удалить папку с существующим файлом")


# q = NewRoot(dir_path='07.08.24/')
# q_1 = NewRoot(dir_path='19.07.24 копия/')

#
# q_2 = NewRoot(dir_path='2024-09-07 05.09.24/')
# print(q_2)


# q_300724 = NewRoot(dir_path='2024-04-23(пф)/')
q_111024 = NewRoot(dir_path='2024-10-06 6.10.24/')
