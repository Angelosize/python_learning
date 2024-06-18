ip=eval(input('请问你要输出至的偶数是多少:'))
aba=[i for i in range(1,ip+1) if i%2==0]
summ=0
for num,it in enumerate(aba,start=1):
    print(num,'---->',it)
    summ+=it
print(f'1-{ip}的偶数和为',summ)

ip=eval(input('请问你要输出至的奇数是多少:'))
aba=[i for i in range(1,ip+1) if i%2==1]
summ=0
for num,it in enumerate(aba,start=1):
    print(num,'---->',it)
    summ+=it
print(f'1-{ip}的奇数和为',summ)

ip=eval(input('请问你要输出至的数是多少:'))
aba=[i for i in range(1,ip+1)]
for num,it in enumerate(aba,start=1):
    print(num,'---->',it)
print(f'1-{ip}的自然数数和为',(1+ip)*ip//2)