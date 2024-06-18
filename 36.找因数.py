from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
def find_factor(number:int) ->list:
    back_lst=[]
    if type(number)!=int:
        raise TypeError("function 'find_factor' only can find factors of type 'int'")
    if number<1:
        raise ValueError("function 'find_factor' can't find its factor")
    if is_prime(number):
        return [1,number]
    for i in range(1,number+1):
        if number % i == 0:
            back_lst.append(i)
    
    return back_lst
print(find_factor(999))
for i in range(1,101):
    if len(find_factor(i))==10:
        print(i)
        


