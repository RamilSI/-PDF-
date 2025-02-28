from googletrans import Translator
# from zadachki import q3_new

q4 = "i   h o p e   y o u   d i d n t   t r a n s l a t e   i t   b y   h a n d .   t h a t s   w h a t   c o m p u t e r s  ' \
     ' a r e   f o r .   d o i n g   i t   i n   b y   h a n d   i s   i n e f f i c i e n t   a n d   '             " \
     "' t h a t ' s   w h y   t h i s   t e x t   i s   s o   l o n g .   u s i n g   s t r i n g . m a k e t r a n s" \
     " ( )  " \
     " i s   r e c o m m e n d e d .   n o w   a p p l y   o n   t h e   u r l ."

translator = Translator()

source_lang = translator.detect(q4).lang
print(f'Определен язык введенного текста: {source_lang}')


result = translator.translate(q4, dest = 'ru')

print(result)