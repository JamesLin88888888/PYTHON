g = 5

def f1():
    
    print(g)
    
    
f1()
print('g =', g)

def f2():
    print(g)
    g = 10
    print(g)
f2()
print(g)
