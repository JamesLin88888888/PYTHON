def even_numbers():
    n = 0
    for i in range(6):
        yield n
        n += 2

even_gen = even_numbers()
'''
for num in even_gen:
    print(num)
'''

try:
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    print(next(even_gen))
    
    print(next(even_gen))
except:
    print('有超出生成器能產生資料的範圍')
    
print('hello')
