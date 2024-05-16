i=9; j=2
def cal(n):
    '高生哥寫的程式'
    # i = 3
    # j = 10
    global i,j
    i = 5
    j = 7
    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    def mut(a,b):
        return a*b

    def div(a,b):
        return a/b
    arg=(add,sub,mut,div)
    
    fun= arg[n]
    return fun(i,j)

k=cal(0)
print(k)
print('i=', i, 'j=', j)

print(cal.__doc__)