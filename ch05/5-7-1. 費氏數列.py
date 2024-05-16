num = int(input('輸入求第幾項費氏數列？'))

a = 1
b = 1
print('第', 1, '項：', a)
for i in range(2, num+1):
    a, b = b, a+b
    print('第', i, '項：', a)
print()

a = 1 # 第 1 項 
b = 1 # 第 2 項
print('第', 1, '項：', a)
print('第', 2, '項：', b)
for i in range(3, num+1):
    c = a + b # 前兩項和
    print('第', i, '項：', c)
    a = b
    b = c    
print()
   

fib_seq = [1, 1]
for i in range(2, num):
    fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
print(fib_seq)