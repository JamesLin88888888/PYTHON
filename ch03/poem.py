
poem = '春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。'
print('原唐詩：', poem)

#poem = poem.replace('。', '').replace('，', '')
poem = poem.replace('。', '')
poem = poem.replace('，', '')
print('原唐詩(無標點符號)：', poem)

list1 = list(poem)
print(list1)

set1 = set(list1)
print(set1)