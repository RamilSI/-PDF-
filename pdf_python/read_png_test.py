import easyocr

"""
Код получает на вход изображение с текстом и с помощью easyocr распознаёт текст распознанный текст должен на изображении 
выделяться рамкой и отображаться через opencv.
"""


def text_recognation(file_path):
    reader = easyocr.Reader(['ru'])
    result = reader.readtext(file_path)
    return result


def main():
    file_path = input('Enter path: ')
    text_recognation(file_path=file_path)


if __name__ == '__main__':
    main()


