i=0
while i<3:
    name=input('请输入您的姓名:')
    pwd=input('请输入您的密码:')
    if name=='Angelo' and pwd=='lag130814':
        print('系统正在登录')
        print('-'*50)
        print('登录成功')
        i=8
    else:
        if i<2:
            print('用户名或密码错误,您还有',2-i,'次机会')
        i+=1
if i==3:
    print('对不起,三次都输错了')