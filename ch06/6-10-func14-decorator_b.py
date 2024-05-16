# 裝飾器 a1，要裝飾一個傳入的函式 func
def a1(func):
    print('1')
    return func

# 裝飾器 a2，要裝飾一個傳入的函式 func
def a2(func):
    print('2')
    return func

# 裝飾器 a3，要裝飾一個傳入的函式 func
def a3(func):
    print('3')
    return func

@a1
@a2
@a3
# 原本的函式
def b():
    print('go!!!')
    


# 呼叫經裝飾的函式b
b()

b()
