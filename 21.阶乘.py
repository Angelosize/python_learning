def fact(i):
    if i==1:
        return 1
    else:
        return i*fact(i-1)
a=eval(input('请问你要算哪个数的阶乘(最高999):'))
print(fact(a))