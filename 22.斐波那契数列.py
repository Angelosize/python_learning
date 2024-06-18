def Fibonacci(number):
    if number==1 or number==2:
        return 1
    else:
        return Fibonacci(number-1)+Fibonacci(number-2)
ip=eval(input('请输入您要查找斐波那契数列的项数:'))# 不要输入50以上的数,会卡的
for i in range(1,ip+1):
    print(Fibonacci(i),end='\t')
#1,1,2,3,5,8,13……