def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mut(a,b):
    return a*b

def div(a,b):
    return a/b

def cal(n,*arg):
    fun= arg[n]
    i=8
    j=3
    return fun(i,j)

k=cal(2,add,sub,mut,div)
print(k)

arg=(add,sub,mut,div)
print(cal(1,*arg))

'''
#%% 2
i=9; j=2
def cal(n):
    global i,j
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
'''