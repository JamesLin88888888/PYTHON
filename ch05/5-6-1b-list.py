odd = [num for num in range(1,11) if (num % 2) == 1 ]
print(odd)


i = range(1, 3)
j = range(1, 4)
mul = [(x, y) for x in i for y in j]
print(mul)

for x, y in mul:
    print(x, y)
    

muls = [(i, j, i*j) for i in range(1, 10) for j in range(1, 10)]
for mul in muls:
    print(mul[0], 'x', mul[1], '=', mul[0])