def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()

for i in range(10):
    print(next(fib_gen))

fib_gen = fibonacci()
for i, fib in enumerate(fib_gen):
    if i==20:
        print(i, fib)