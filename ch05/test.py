for i in range(1, 97):
    j = i + 31
    c = chr(j)
    print(c, end=' ')
    if i % 16 == 0:
        print()
