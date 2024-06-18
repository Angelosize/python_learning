#the first method
l=eval('['+input('请输入员工的二位数年份,如果是多个请用英文逗号分隔')+']')
for i in range(len(l)):
    if str(l[i]) != '0':
        if l[i]<14:
            l[i]='20'+str(l[i])
        else:
            l[i]='19'+str(l[i])
    else:
        l[i]='200'+str(l[i])
print(l)
#the second method
p=eval('['+input('请输入员工的二位数年份,如果是多个请用英文逗号分隔')+']')
for i,v in enumerate(p):
    if str(v) != '0':
        if p[i]<14:
            p[i]='20'+str(v)
        else:
            p[i]='19'+str(v)
    else:
        p[i]='200'+str(v)
print(p)
print('Made by Angelo_size')