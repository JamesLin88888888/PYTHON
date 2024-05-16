

print('所有偶數')
for i in range(101):
    if i % 2 == 0:
        print(i, end=', ')
print()
        

print('所有奇數')
for i in range(101):
    if i % 2 == 1:
        print(i, end=', ')
print()
    

print('所有偶數')
for i in range(0, 101, 2):
    print(i, end=', ')

print()
print('所有奇數')
for i in range(1, 101, 2):
    print(i, end=', ')
    