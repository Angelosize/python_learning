#反直角三角形
row=int(input('请输入反直角三角形行数:'))
for i in range(1,row+1):
    print('*'*(row+1-i))
print('-'*30)
#等腰
ro=int(input('请输入等腰三角形行数:'))
for i in range(1,ro+1):
    for j in range(1,ro+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
print('-'*30)
#实心菱形
r=eval(input('请输入实心菱形行数:'))
while r%2==0:
    print('菱形行数不能为偶数,重新输入菱形的行数')
    r=eval(input('请输入实心菱形行数:'))
upr=(row+1)//2
for i in range(1,upr+1):
    for j in range(1,upr+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        print('*',end='')
    print()
btr=row//2
for i in range(1,btr+1):
    for j in range(1,1+i):
        print(' ',end="")
    for k in range(1,2*btr-2*i+2):
        print('*',end='')
    print()
print('-'*30)
#空心

r=eval(input('请输入空心菱形行数:'))
while r%2==0:
    print('菱形行数不能为偶数,重新输入菱形的行数')
    r=eval(input('请输入空心菱形行数:'))
upr=(row+1)//2
for i in range(1,upr+1):
    for j in range(1,upr+1-i):
        print(' ',end='')
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
btr=(row-1)//2
for i in range(1,btr+1):
    for j in range(1,1+i):
        print(' ',end="")
    for k in range(1,2*btr-2*i+2):
        if k==1 or k==2*btr-2*i+1:
            print('*',end='')
        else:
            print(' ',end='')
    print()




print('Made by Angelo_size')