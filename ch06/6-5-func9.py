def add(a, b):
    return a + b

def mul(a, b):
    return a * b


def run(func, x, y):
    return func(x, y)


k = run(add, 10, 20)
print('k=', k)

k = run(mul, 10, 20)
print('k=', k)

xfunc = mul
k = xfunc(10, 20)
print('k=', k)
