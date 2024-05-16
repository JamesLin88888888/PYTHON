
# 客製化的函式
def myFunc(e): # e is a tuple
    #return e[1] # return second element in this tuple
    return ord(e[0][-1])
    
    

list1 = [('Sean', 29), ('Ant', 49), ('Rodman', 30)]
print('Before sorting...')
print(list1)

list1.sort(reverse=True, key=myFunc)

print('After sorting...')
print(list1)
