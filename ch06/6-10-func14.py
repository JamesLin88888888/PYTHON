# 裝飾器函式
def debug(arg_func):
    def inner_func(*args, **kwargs):
        print('正在執行函式', arg_func.__name__)
        print('函式的說明文件為', arg_func.__doc__)
        print('位置引數', args)
        print('關鍵引數', kwargs)
        return arg_func(*args, **kwargs)
    return inner_func

# 原本的函式
def add(a, b):
    '回傳a加b的結果'
    return a+b


xfun = debug(add)
print(xfun(1, b=2))
# print(add(1, b=2))

@debug
def add(a, b, c):
    '回傳a+b+c的結果'
    return a+b+c
print(add(1, 2, c=3))

@debug
def mul(a, b):
    '回傳a*b的結果'
    return a*b
print(mul(5, 3))
