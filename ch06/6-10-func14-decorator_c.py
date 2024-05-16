def a(func):
    def c(n):
          print('makeup...')
          return func(n)
    return c

@a
def b(msg):
    print(msg)
    
b('go!!!')