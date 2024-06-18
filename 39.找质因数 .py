from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def find_prime_factor(number:int):
    back_lst=[]
    another_lst=[]
    if type(number)!=int:
        raise TypeError("function 'find_factor' only can find factors of type 'int'")
    if number<2:
        raise ValueError("function 'find_factor' can't find its factor")
    num=number+1-1
    if is_prime(number):
        return [(number,1)]
    while num!=1:
        for i in range(2,num):
            if num % i == 0 and is_prime(i):
                another_lst.append(i)
                num//=i
                if is_prime(num):
                    another_lst.append(num)
                    break
        if is_prime(num):
            break
    for i in another_lst:
    
        c=another_lst.count(i)
        back_lst.append((i,c))
        for i1 in range(c):
            another_lst.remove(i)
    return back_lst

print(find_prime_factor(50))