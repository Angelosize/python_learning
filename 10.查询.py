pwd='y'
print('-'*10,'欢迎使用格格查询功能','-'*10)
print('输入0:退出系统')
print('输入1:查询当前余额')
print('输入2:查询当前剩余流量')
print('输入3:查询当前剩余通话时长')
while pwd=='y':
    
    choice=eval(input('请输入您要执行的操作:'))
    if choice==1:
        print('当前余额为:大聪明元')
    elif choice==2:
        print('当前剩余流量为:大聪明GB')
    elif choice==3:
        print('当前剩余通话时长为:大聪明min')
    elif choice==0:
        print('-'*10,'感谢您的支持,欢迎下次使用','-'*10)
        print('退出成功')
        break
    else:
        print('您的输入有误,请重新输入')
    pwd=input('还要继续操作吗?(输入y/n)')
else:
    print('-'*10,'感谢您的支持,欢迎下次使用','-'*10)
    print('退出成功')


print('Made by Angelo_size')