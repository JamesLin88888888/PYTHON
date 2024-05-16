lang={'你好':'Hello',
      '謝謝':'Thanks'}

for ch, en in lang.items():
    print('中文為', ch, '英文為', en)

for item in lang.items():
    # item is a tuple
    print('中文為', item[0], '英文為', item[1])
    
for i, item in enumerate(lang.items()):
    print(i, item[0], item[1])

for ch in lang.keys():
    print(ch,lang[ch])
    
for i, ch in enumerate(lang.keys()):
    print(i, ch,lang[ch])    
    
for en in lang.values():
    print(en)