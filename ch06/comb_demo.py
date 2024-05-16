
def comb(m, n):
    if n==0 or m==n:
        return 1
    else:
        return comb(m-1, n) + comb(m-1, n-1)

print(comb(10, 3))