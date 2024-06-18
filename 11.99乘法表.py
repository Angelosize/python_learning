a=eval(input('请问要输出至多少:'))
for i in range(1,a+1):
    for j in range(1,i+1):
        if j==i:
            print(str(j)+'×'+str(i)+'='+str(i*j))
        else:
            print(str(j)+'×'+str(i)+'='+str(i*j),end=',')


print('Made by Angelo_size')
    