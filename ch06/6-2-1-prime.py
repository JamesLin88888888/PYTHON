def is_prime(num):
    for i in range(2, num):
        if num % i == 0:  # 整除，i 是 n 的因數，所以 n 不是質數。
            return False
    return True     # 都沒有人能整除，所以 n 是質數。

for i in range(1, 101):
    if is_prime(i):
        print(i, sep=', ')