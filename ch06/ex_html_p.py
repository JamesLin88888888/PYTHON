def p_deco(func):
    def ptag(s):
        return '<p>'+str(func(s))+'</p>'
    return ptag
@p_deco
def phtml(s):
    return 'Hello,'+s

text = input('請輸入段落文字：')
print(phtml(text))
