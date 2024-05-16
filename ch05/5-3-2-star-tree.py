h = 8

for i in range(1, h + 1):
    numSpaces = h - i
    for j in range(numSpaces):
        print(' ', end='')
    for j in range(i):
        print('* ', end='')
    if i < h :
        print()
        print()
