# 原本的函式
def b():
    print('go!!!')


# 裝飾器 a，要裝飾一個傳入的函式 func
def a(func):
    print('makeup...')
    return func


# 呼叫尚未裝飾的函式b
b()
print()

# 裝飾函式b
b = a(b)
# 呼叫經裝飾的函式b
b()