# print (2**38)

import string
q = string.ascii_lowercase
print(q)

q1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb ' \
     'rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

t = []
for el in q1:
    if el in q:
        p = ord(el)+2
        t.append(chr(p))
    else:
        t.append(el)
q3 = ' '.join(t)

q3_new = q3.replace('{', 'a').replace('|', 'b')
print(q3)
print(q3_new)
# for el in q3:
#     if el == '{':
#         print('есть такой знак')
