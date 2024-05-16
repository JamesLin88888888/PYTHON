# lut = look-up table
lut1 = {chr(key): chr(key+1) for key in range(97, 97+26) if key % 2 == 1}
lut2 = {chr(key): chr(key-1) for key in range(97, 97+26) if key % 2 == 0}

print(lut1)
print(lut2)

lut_merged = {}
lut_merged.update(lut1)
lut_merged.update(lut2)
print(lut_merged)


msg = 'an apple a day keeps doctor a way.' # input('請輸入一段英文文字: ')
msg = msg.lower()
msg_encrypted = ''
for c in msg:
    if c in lut_merged.keys():
        msg_encrypted += lut_merged[c]
    else:
        msg_encrypted += c

print('original:', msg)
print('encrypted: ', msg_encrypted)
