
with open('pdfText.txt', 'r') as file:
    line = file.read()
t = ''
for x in range(0, len(line), 173):
    t +=(line[x:x+173])+'\n'

with open('read_txt_1', 'w') as file_obj:
    file_obj.write(t)




