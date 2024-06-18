s=set()
ii=eval(input('请问你要输入几位好友的姓名和手机号:'))
for i in range(1,ii+1):
    info=input(f'请输入第{i}位好友的姓名和手机号:')
    s.add(info)
for it in s:
    print(it)
print('Made by Angelo_size')