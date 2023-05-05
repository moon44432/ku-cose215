import re

f = open("probelm2.html", 'r', encoding='UTF-8')
html = f.read()

p = re.compile("<br\/>[\n\t ]*<a href=\"mailto:([\w]+)[ ]*(@[\w]+[.[\w]+]*)\"")
q = re.compile("<b>전화번호:<\/b>[\n\t ]*\t([0-9]{2,3}-[0-9]{3,4}-[0-9]{4})")
r = re.compile("<b>홈페이지:<\/b>[\n\t ]*<a href=\"([-a-zA-Z0-9@:%._\\\/+~#=]+)\"")

mails = re.finditer(p, html)
phonenums = re.finditer(q, html)
homepages = re.finditer(r, html)

output = "# Result over html file\n\n"

output += "E-mail: "
for i in mails:
    output += (i.group(1) + i.group(2) + ", ")
output = output[:-2]
output += "\n\n"

output += "Phone Number: "
for i in phonenums:
    output += (i.group(1) + ", ")
output = output[:-2]
output += "\n\n"

output += "HomePage: "
for i in homepages:
    output += (i.group(1).rstrip("/") + ", ")
output = output[:-2]

print(output)
f.close()

'''
# Result over html file

E-mail: example@korea.ac.kr, ... , example@korea.ac.kr

Phone Number: 02-XXXX-XXXX, ..., 02-XXXX-XXXX

HomePage: https://example.korea.ac.kr, ... , https://example.korea.ac.kr
'''