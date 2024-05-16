import random

num_A = random.randint(1,99)
num_B = int(input('請猜一個數字：'))

while num_B != num_A:
    if num_B > num_A:
        print('猜小一點')
    elif num_B < num_A:
        print('猜大一點')
    num_B = int(input('請猜一個數字：'))

print('你猜對了')
    

