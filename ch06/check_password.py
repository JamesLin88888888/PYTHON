def check_password(pwd):
    if pwd.isdigit() or pwd.isalpha():
        if len(pwd) < 6:
            print('不安全的密碼')
        elif len(pwd) >= 6:
            print('可能是安全的密碼')
    else: # pwd 為英數字組成
        if len(pwd) < 6:
            print('不安全的密碼')
        elif 10 > len(pwd) >= 6: # len(pwd) >= 6 and len(pwd) < 10
            print('安全的密碼')
        else: # len(pwd) >= 10
            print('非常安全的密碼')


pwd = '123a' # input('請輸入密碼：')
check_password(pwd)

