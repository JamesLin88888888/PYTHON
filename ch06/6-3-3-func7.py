# 可變動長度的參數列
# in python, positional arguments
def func1(*args):
    ls = list(args)
    print(ls)
    ls[1] = 5
    print(ls)
    

func1(1, 2, 3)
# func1()
# func1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def func2(**kwargs):
    for key, value in kwargs.items():
        print(f'kwargs[{key}]={value}')
    # print('關鍵字引數為', kwargs)

func2(a=1, b=2)
func2(test1=1, test2=2, sep='-')

def func3(start, *args, **kwargs):
    print("start=", start)
    print("位置引數為", args)
    print("關鍵字引數為", kwargs)
func3(1, 2, 3, a=4, b=5)
