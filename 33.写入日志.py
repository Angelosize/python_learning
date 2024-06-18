import time,os
def show_info():
    print('输入提示数字,执行相应的操作:0.退出  1.查看登录日志  2.清空日志\n')
def write_loginfo(un):
    with open('python_files/log.txt','a',encoding='utf-8') as file:
        s=f'用户名:{un},登陆时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')

def write_quit_loginfo(un):
    with open('python_files/log.txt','a',encoding='utf-8') as file:
        s=f'用户名:{un},退出时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)
        file.write('\n')

def read_loginfo():
    with open('python_files/log.txt','r',encoding='utf-8') as file:
        a=file.read()
        if a=='':
        
            print('日志为空\n')
        file.seek(0)
        while True:
            line=file.readline()
            if line=='':
                break
            else:
                print(line)
if __name__=='__main__':
    print('-'*50)
    name=input('请输入您的姓名:')
    print()
    pwd=input('请输入您的密码:')
    print()
    name_and_pwd_dict={'李安格':'130814','吴淼':'147258','李渭滨':'','薛丽文':'555555'}#可以存放大家的名字和密码
    if name_and_pwd_dict.get(name)==pwd:
        print('登录成功')
        print()
        write_loginfo(name)
        show_info()
        num=eval(input('请输入要操作的数字:'))
        while True:
            if num==0:
                print('\n退出成功\n','-'*50,sep='')
                write_quit_loginfo(name)
                break
            elif num==1:
                print('\n查看登录日志\n')
                read_loginfo()
                show_info()
            elif num==2:
                print('\n清空日志成功\n')
                os.remove('python_files/log.txt')
                with open('python_files/log.txt','a',encoding='utf-8') as file:
                    pass
            else:
                print('\n对不起,您输入的数字有误\n')
                show_info()
            num=eval(input('请输入要操作的数字:'))
    else:
        print('用户名或密码错误')