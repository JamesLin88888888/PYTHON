存款金額 = int(input('請輸入存款金額？'))
年利率 = float(input('請輸入年利率？'))
目標金額 = int(input('請輸入目標金額？'))
year = 0
本利和 = 存款金額
while 本利和 <= 目標金額:
  本利和 = 本利和 * (1 + 年利率 / 100)
  year = year + 1
print("第", year, "年後本利和為", 本利和, "超過", 目標金額)
