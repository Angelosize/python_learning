lst=[]
fl=open('python_files\素数\素数.txt','w')
from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
t=eval(input('请问要输出1到多少的素数:'))
for i in range(1,t+1):
    if is_prime(i)==True:
        print(i,file=fl,end='\n')
        #print(i)
        lst.append(i)
        
print(f'一共有{len(lst)}个')
fl.close()
#python_files\素数\1-1000000素数.txt