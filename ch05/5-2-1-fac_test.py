n = int(input('請輸入一個數值'))

result = 1
i = 1
while i <= n:
    result = result * i
    print('i=', i)
    i = i + 1
    
# n = 5
# 5! = 
print(f'{n}!={result}')