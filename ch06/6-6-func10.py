import random

def add(x, y):
    return x+y

def run(func, x, y):
    return func(x, y)

# 不用 lamda 函式設計
k = run(add, 10, 20)
print('[no lamda] k=', k)


# lamda 函式設計
add = lambda a,b: a+b
k = run(add, 10, 20)
print('k=', k)

k = run(lambda a,b: a*b, 10, 20)
print('k=', k)

test = lambda a,b: a-b
k = run(test, 10, 20)
print('k=', k)

myrand = lambda a,b: random.randint(a, b)
k = run(myrand, 10, 20)
print('k=', k)

# 容器生成式
mylist = [x for x in range(0, 20) if x%2==0]
print(mylist)

# for 迴圈的寫法
ls = []
for x in range(5):
    ls.append(x)

#容器生成式
ls = [x for x in range(5)]

