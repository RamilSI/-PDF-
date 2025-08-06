import hashlib
import os


def remove_duplicates(folder_path):
    hash_dict = []

    for root, dirs, files in os.walk(folder_path):  # проход по директории, по папкам, по файлам
        print(f' это root: {root} это dirs: {dirs} это files: {files}')
        for file_name in files:
            file_path = os.path.join(root, file_name)   # используя os.path.join записываю полный путь к файлу
            print(f' это путь после join: {file_path}')
            with open(file_path, 'rb') as file:     #
                file_hash = hashlib.md5(file.read()).hexdigest()
                print(f'это hashlib: {file_hash}')
                if file_hash not in hash_dict:
                    hash_dict.append(file_hash)
                else:
                    print(f"Удаление дубликата: {file_name}")

    print(f' это hash_dict: {hash_dict}')


if __name__ == '__main__':
    folder_path = '/Users/admin/Library/CloudStorage/GoogleDrive-rml7771@gmail.com/Мой диск/Временный файлообменник/' \
                  'афипский нпз/ОПИ/чертежи афип от жени/Фото с телефона '
    # for root, dirs, files in os.walk(folder_path):
    #     print(f'это root: {root} это dirs: {dirs} а это FILES: {files}')
    remove_duplicates(folder_path)

