# 字串 < 比較原則
# 每一字母進行比較
# 只要滿足 < 條件，即回傳True
str1 = 'SEan'
str2 = 'sean'
result = str1 < str2
print('str1 =', str1)
print('str2 =', str2)
print('str1 < str2 = ', result )

str1 = 'seAn'
str2 = 'sean'
result = str1 < str2
print('str1 =', str1)
print('str2 =', str2)
print('str1 < str2 = ', result )