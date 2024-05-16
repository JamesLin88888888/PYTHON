
todos = list()

task = input('請輸入工作項目：')
todos.append(task)
task = input('請輸入工作項目：')
todos.append(task)
task = input('請輸入工作項目：')
todos.append(task)
task = input('請輸入工作項目：')
todos.append(task)
task = input('請輸入工作項目：')
todos.append(task)

print('取出的第一項：', todos.pop(0))
#todos.remove(todos[0])
print('取出的第二項：', todos.pop(0))
#todos.remove(todos[0])
print('剩下的元素：', todos)
last_index = len(todos)-1
print('最後一個元素：', todos[last_index])

#del todos[0]
#del todos[0]

'''
print(task1)
print(task2)
print(task3)
print(task4)
print(task5)
'''