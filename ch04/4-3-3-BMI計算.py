w = float(input('請輸入體重(KG)？'))
h = float(input('請輸入身高(CM)？'))
h = h / 100
h = h ** 2
bmi = w/h
print('BMI為', bmi)
if bmi < 18:
    print('體重過輕')
elif bmi < 24:
    print('體重正常')
elif bmi < 27:
    print('體重過重')
else:
    print('體重肥胖')

