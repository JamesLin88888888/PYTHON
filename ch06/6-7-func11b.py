def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

even_gen = even_numbers()

for num in even_gen:
    print(num)

'''
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
print(next(even_gen))
'''

'''

for i, evennum in enumerate(even_gen):
    if i > 10:
        break
    print(i, evennum)
    '''

