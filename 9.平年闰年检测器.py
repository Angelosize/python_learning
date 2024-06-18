inpt=eval(input('请输入一个四位数年份:'))
while inpt>9999 or inpt<1000:
    print('年份应为四位数，请重新输入')
    inpt=eval(input('请输入一个四位数年份:'))
if (inpt%4==0 and inpt%100!=0) or inpt%400==0:
    print(inpt,'年是闰年')
else:
    print(inpt,'年是平年')


print('Made by Angelo_size')