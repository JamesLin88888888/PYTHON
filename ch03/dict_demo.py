
my_dict = {'hello': '哈囉',
           'name': '姓名',
           'apple': '蘋果'}

print('目前字典支援的英文單字：')
for en in my_dict.keys():
    print(en)
    

print()
print('整本字典：')
for item in my_dict.items():
    en, ch = item
    print(en, '->',ch)
    
    
word = input('請輸入一個英文單字：')
print('其中文為：', my_dict.get(word, '不支援此單字'))

print('謝謝您')