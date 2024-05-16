cost = int(input('請輸入購買金額？'))
if cost >= 2000:
    print('打折後的價格：', end='')
    print(cost * 0.9)
else:
    print('原價格：', end='')
    print(cost)
