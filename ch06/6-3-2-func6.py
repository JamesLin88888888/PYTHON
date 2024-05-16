from datetime import datetime # 從 datetime 套件，引用 datetime 類別
from datetime import date # 從 datetime 套件，引用 date 類別

def ymd():
    now = datetime.now()
    return (now.year, now.month, now.day)

'''
y, m, d = ymd()
print(y,m,d)

mytime1 = datetime(1990, 1, 25, 13, 30, 0)
print(mytime1)

mytime2 = datetime(1990, 1, 30, 8, 0, 0)
print(mytime2)

deltatime = mytime2 - mytime1 # timedelta
print('deltatime.total_seconds()', deltatime.total_seconds())

dtstr = '2019-12-04'
dt = date.fromisoformat(dtstr)
print(dt)
'''

mydict1 = {1: 'first', 2:'second'}
mydict2 = {3: 'first', 2:'second'}

print(mydict2 == mydict1)


dt_enroll = datetime(1990, 8, 1)
dt_graduate = datetime(1995, 8, 1)
mydict = {dt_enroll: '入學', dt_graduate: '畢業'}
print(mydict)

dt_temp= datetime(1990, 8, 1)
print(mydict[dt_temp])

# dt_temp= datetime(1990, 8, 1, 23, 10, 10)
# print(mydict[dt_temp])
