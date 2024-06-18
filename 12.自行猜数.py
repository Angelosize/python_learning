import random
p=1
t=eval(input('要猜1到多少的数:'))
a=random.randint(1,t)
print('这是一个1到'+str(t)+'之间的数')
g=eval(input('猜猜这个数是多少:'))
while g!=a:
    if g>a:
        print('猜大了')
    if g<a:
        print('猜小了')
    g=eval(input('猜猜这个数是多少:'))
    p+=1
print('猜对了,用了'+str(p)+'次')
print('Made by Angelo_size')