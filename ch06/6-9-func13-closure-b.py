def count():
    a = []
    def avg(val):
        a.append(val)
        print(a)
        return sum(a) / len(a)
    return avg

test = count()
print('avg=', test(10))
print('avg=', test(11))
print('avg=', test(12))
