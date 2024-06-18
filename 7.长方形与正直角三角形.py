for i in range(1,4):
    for j in range(1,5):
        print('*',sep='',end='')
    print()#换行
print('-'*40)

for i in range(1,6):
    print('*'*i,sep='')
print('-'*40)

for i in range(1,7):
    for j in range(1,7-i):
        print('*',sep='',end='')
    print()
print('-'*40)