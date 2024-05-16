def BMI(w, h):
    return w/(h*h)

def outputMessage(bmi):
    print('BMI為', bmi)
    if (bmi < 18):
        print('體重過輕')
    elif (bmi < 24):
        print('體重正常')
    elif (bmi < 27):
        print('體重過重')
    else:
        print('體重肥胖')    

for i in range(5):
    w = float(input('請輸入體重(KG)？'))
    h = float(input('請輸入身高(CM)？'))
    h = h / 100
    
    bmi = BMI(w, h)
    outputMessage(bmi)