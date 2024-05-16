a=[['早安','Good Morning'],  # (key1, value1)
   ['你好',       'Hello'],  # (key2, value2)
   ['早安','Good Evening']]  # (key3, value3)

dict1=dict(a)
print(dict1)

b=[('早安','Good Morning'),('你好','Hello')]
dict2=dict(b)
print(dict2)

c=(['早安','Good Morning'],['你好','Hello'])
dict3=dict(c)
print(dict3)

d=(('早安','Good Morning'),('你好','Hello'))
dict4=dict(d)
print(dict4)
