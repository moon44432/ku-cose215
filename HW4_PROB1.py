import re

f = open("input.txt", 'r', encoding='UTF-8')
words = f.read().split()
found = []
print(words)

p = re.compile("([AB][^AB]*){4}[AB]")
q = re.compile("[AB]{5}")

for i in words:
    m = p.search(i)
    if m is not None:
        bin = []
        for ch in m.group():
            if ch == 'A' or ch == 'B':
                bin.append(chr(ord(ch) - ord('A') + ord('0')))
        binstr = (''.join(bin))

        s = i.replace(m.group(), chr(int(binstr, 2) + ord('a')))
        found.append(s)
    else:
        found.append(i)

print(''.join(found))
f.close()