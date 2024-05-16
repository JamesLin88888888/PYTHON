sh = ['牛奶', '蛋', '咖啡豆']

# for-i look
for i in range(0,len(sh)):
    print (i, sh[i])

# for-each loop
for item in sh:
    print(item)
    
    
for i, name in enumerate(sh): # , start=1
    print(i, name)