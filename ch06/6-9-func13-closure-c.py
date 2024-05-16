def count():
    a = 1
    def avg(val):
        nonlocal a
        a = a + val
        return a
    return avg

test = count()
print(test(10))
print(test(11))
print(test(12))
