lang={'早安':'Good Morning',
      '你好':'Hello',
      '晚安':'Good Evening'}

for ch, en in lang.items():
    print('--------')
    print('中文為', ch, '英文為', en)
    print('----', ch, '---', en)
print(lang)


for item in lang.items():
    ch, en = item
    print('中文為', ch, '英文為', en)
    
    
for ch in lang.keys():
    print(ch,lang[ch])

for en in lang.values():
    print(en)

