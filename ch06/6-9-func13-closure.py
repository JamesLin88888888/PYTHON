
def a(msg):
    i = '!!!'
    def b():
        print(msg+i)
    return b

s = a('hello')
s()