from math import *
import time
from typing import Any,List,Literal,Iterable
from copy import deepcopy
from itertools import filterfalse
from words import words
import re
def is_prime(number:int) -> bool:
    if number == 1:
        return False
    for i in range(2,int(sqrt(number))+1):
        if number % i == 0:
            return False
    return True
def is_only_prime_factor(number:int,allowable_factor:list[int]) -> bool:
    if number<=1:
        return False
    f_list=prime_factor(number)
    for i in allowable_factor:
        try:
            while True:
                f_list.remove(i)
        except:
            pass
    if f_list!=[]:
        return False
    return True
def factor(number:int) ->list:
    back_lst=[]
    if type(number)!=int:
        raise TypeError("function 'factor' only can find factors of type 'int'")
    if number<1:
        raise ValueError("function 'factor' can't find its factor")
    if is_prime(number):
        return [1,number]
    for i in range(1,number+1):
        if number % i == 0:
            back_lst.append(i)
    
    return back_lst
def prime_factor(number:int,do_return_tuples:bool=False) -> (list[tuple[int,int]] | list[int]):
    back_lst=[]
    another_lst=[]
    if type(number)!=int:
        raise TypeError("function 'factor' only can find factors of type 'int'")
    if number<2:
        raise ValueError("function 'factor' can't find its factor")
    num=number+1-1
    if is_prime(number):
        if do_return_tuples:
            return [(number,1)]
        else:
            return [number]
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
    if not do_return_tuples:
        return another_lst
    for i in another_lst:
    
        c=another_lst.count(i)
        back_lst.append((i,c))
        for _ in range(c):
            another_lst.remove(i)
    

    return back_lst
def co_prime(a:int,b:int) -> bool:
    if set(factor(a))&set(factor(b))=={1}:
        return True
    return False
def generate_prime_list(start:int,end:int,IncludeStop:bool=True) -> list:
    if IncludeStop:
        my_range=range(start,end+1)
    else:
        my_range=range(start,end)
    back_list=[]
    for i in my_range:
        if is_prime(i):
            back_list.append(i)
    return back_list
def get_minus(a_list:list) -> list[int]:
        return [b-s for s,b in zip(a_list[:-1:],a_list[1::])]
def sum_multiply(thing:Iterable[int]) -> int:
    a=1
    for i in thing:a*=i
    return a
def lowest_common_multiple(*numbers:int) -> int:
    numbers=list(numbers)
    if len(numbers)==2:
        if co_prime(numbers[0],numbers[1]):
            return sum_multiply(numbers)
        my_lst1=[i for i in prime_factor(numbers[0])]
        my_lst2=[i for i in prime_factor(numbers[1])]
        bind_list=[]
        # for i in prime_factor(numbers[0]):
        #     my_lst1.append(i)
        # for i in prime_factor(numbers[1]):
        #     my_lst2.append(i)
        my_lst1_a=my_lst1.copy();my_lst2_a=my_lst2.copy()
        for i in my_lst1_a:
            if (i in my_lst1) and (i in my_lst2):
                my_lst1.remove(i);my_lst2.remove(i);bind_list.append(i)
        for i in bind_list:
            my_lst1_a.remove(i)
        return sum_multiply(my_lst2_a+my_lst1_a)
    else:
        a=lowest_common_multiple(*(numbers[1::]))
        return lowest_common_multiple(numbers[0],a)
def greatest_common_divisor(*numbers : int) -> int:
    numbers=list(numbers)
    
    if len(numbers)==2:
        if co_prime(numbers[0],numbers[1]):
            return 1
        my_lst1=[i for i in prime_factor(numbers[0])]
        my_lst2=[i for i in prime_factor(numbers[1])]
        bind_list=[]
        # for i in prime_factor(numbers[0]):
        #     my_lst1.append(i)
        # for i in prime_factor(numbers[1]):
        #     my_lst2.append(i)
        my_lst1_a=my_lst1.copy();my_lst2_a=my_lst2.copy()
        for i in my_lst1_a:
            if (i in my_lst1) and (i in my_lst2):
                my_lst1.remove(i);my_lst2.remove(i);bind_list.append(i)
        return sum_multiply(bind_list)
    else:
        a=greatest_common_divisor(*(numbers[1::]))
        return greatest_common_divisor(numbers[0],a)
def get_multiple(a_list:list) -> list:

    return [b/s for s,b in zip(a_list[:-1:],a_list[1::])]
def find_perfect_number(number_to = 6) -> list[int]: # include number_to
    '''
    include number_to
    '''
    back_list=[]
    if number_to>=6:
        try_number=1
        while (2**try_number-1)*(2**(try_number-1))<=number_to:
            if is_prime(2**try_number-1):
                back_list.append((2**try_number-1)*(2**(try_number-1)))
            try_number+=1
        return back_list

    else:
        return []
def is_perfect_number(number:int=None) -> bool:
    sums=0
    for ij in factor(number):
        if ij!=number:
            sums+=ij
    if sums==number:
        return True
    return False
def is_iterable(thing:Any) -> bool:
    try:
        thing.__iter__()
        return True
    except:
        return False
def turn_float_into_int(iterable:Iterable[float]) -> Iterable[int|float]:
    for num,i in enumerate(iterable):
        if int(i)==i:
            iterable[num]=int(i)
    return iterable
class CantFindPatternError(BaseException):
    def __init__(self):
        super().__init__()
        self.__114514__='surprise!!!'
def find_pattern(lst:list,continue_steps:int=1):
    if len(lst)<=3:
        raise CantFindPatternError("can't find pattern with list which its length is smaller than 4")
    def fun1():
        counter=0
        for s,b in zip(lst[:-1:],lst[1::]):
            if s == lst[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(lst)-1:
            raise Exception([1 , p , lst[-1]])
        '''------等差数列------'''
    def fun2():
        counter=0
        for s,b in zip(lst[:-1:],lst[1::]):
            if s == lst[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(lst)-1:
            raise Exception([2 , p , lst[-1]])
        '''------等比数列------'''
    def fun3():
        minus_list=get_minus(lst)
        counter=0
        for s,b in zip(minus_list[:-1:],minus_list[1::]):
            if s == minus_list[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(minus_list)-1:
            raise Exception([3 , p , lst[-1] , minus_list[-1]])
        '''------差中等差------'''
    def fun4():
        minus_list=get_minus(lst)
        counter=0
        for s,b in zip(minus_list[:-1:],minus_list[1::]):
            if s == minus_list[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(minus_list)-1:
            raise Exception([4 , p , lst[-1] , minus_list[-1]])
        '''------差中等比------'''
    def fun5():
        multiple_list=get_multiple(lst)
        counter=0
        for s,b in zip(multiple_list[:-1:],multiple_list[1::]):
            if s == multiple_list[0]:
                p=b-s;counter+=1
            else:
                if b-s==p:
                    counter+=1
        if counter==len(multiple_list)-1:
            raise Exception([5 , p , lst[-1] , multiple_list[-1]])
        '''------比中等差------'''
    def fun6():
        multiple_list=get_multiple(lst)
        counter=0
        for s,b in zip(multiple_list[:-1:],multiple_list[1::]):
            if s == multiple_list[0]:
                p=b/s;counter+=1
            else:
                if b/s==p:
                    counter+=1
        if counter==len(multiple_list)-1:
            raise Exception([6 , p , lst[-1] , multiple_list[-1]])
        '''------比中等比------'''
    def fun7():
        if lst==generate_prime_list(lst[0],lst[-1]):
            raise Exception([7 , lst[-1]])
    def main():
        fun1()
        fun2()
        fun3()
        fun4()
        fun5()
        fun6()
        fun7()
        raise Exception([None])
    try:
        main()
    except Exception as stuff:
        stuff=str(stuff)
        back_lst=[]
        stuff=eval(stuff)
        match stuff[0]:
            case 1:
                for _ in range(continue_steps):
                    stuff[2]+=stuff[1]
                    back_lst.append(stuff[2])
            case 2:
                for _ in range(continue_steps):
                    stuff[2]*=stuff[1]
                    back_lst.append(stuff[2])
                back_lst=turn_float_into_int(back_lst)
            case 3:
                for _ in range(continue_steps):
                    stuff[3]+=stuff[1]
                    stuff[2]+=stuff[3]
                    back_lst.append(stuff[2])
            case 4:
                for _ in range(continue_steps):
                    stuff[3]*=stuff[1]
                    stuff[2]+=stuff[3]
                    back_lst.append(stuff[2])
            case 5:
                for _ in range(continue_steps):
                    stuff[3]+=stuff[1]
                    stuff[2]*=stuff[3]
                    back_lst.append(stuff[2])
            case 6:
                for _ in range(continue_steps):
                    stuff[3]*=stuff[1]
                    stuff[2]*=stuff[3]
                    back_lst.append(stuff[2])
            case 7:
                while len(back_lst)<continue_steps:
                    stuff[1]+=1
                    if is_prime(stuff[1]):
                        back_lst.append(stuff[1])
            case None:
                
                raise CantFindPatternError(f"can't find pattern of list -> {lst}")
        back_lst=turn_float_into_int(back_lst)
        return back_lst
def find_perfect_number(start_number:int=1,number_to :int= 6,include_number_to:bool=True) -> list[int]:
    back_list=[]
    if number_to>=6:
        try_number=start_number
        while (2**try_number-1)*(2**(try_number-1))<=(number_to if include_number_to else number_to-1):
            if is_prime(2**try_number-1):
                back_list.append((2**try_number-1)*(2**(try_number-1)))
            try_number+=1
        return back_list
    else:
        return []
def is_perfect_number(number:int=None) -> bool:
    sums=0
    for ij in factor(number):
        if ij!=number:
            sums+=ij
    if sums==number:
        return True
    return False
def Fibonacci(number:int) -> int:
    if number==1 or number==2:
        return 1
    else:
        return Fibonacci(number-1)+Fibonacci(number-2)
def is_Fibonacci(number:int,return_digit:bool=False) -> (bool|list[bool,int]):
    i=1
    while Fibonacci(i)<=number:
        if Fibonacci(i)==number:
            return True if (not return_digit) else [True,i]
        i+=1
    return False
def permutation(iterable:Iterable[Any]):
    item = iterable
    if len(item)==1:
        return [item]
    res=[]
    for i,x in enumerate(item):
        n=item[:i]+item[i+1:]
        for y in permutation(n):
            res.append(x+y)
    return sorted(list(set(res)))
def re_type(iterable:Iterable) -> Iterable:
    res=iterable
    for n,i in enumerate(res):
        try:
            res[n]=type(iterable)(res[n])
        except:
            pass
        return res
def deduplicate(item:list|tuple):
    a=type(item)
    return a(set(item))
def stralize(iterable:Iterable)->Iterable:
    for i,j in enumerate(iterable):
        iterable[i]=str(j)
    return iterable 
def fact(int:int) -> int:
    i=deepcopy(int)
    a=1
    for j in range(1,i+1):
        a*=j
    return a
def centre(string:str,length:int,way:str='left') -> str:
    if len(string)>length:
        raise ValueError
    blank=length-len(string)
    if blank==0:
        return string
    string_copy=''
    shorter_place=(blank//2)*' '
    longer_place=(blank-blank//2)*' '
    match way:
        case 'left':
            string_copy=shorter_place+string+longer_place
        case 'right':
            string_copy=longer_place+string+shorter_place
    return string_copy
def is_multiple(base:int,number:int) -> bool:
    return not number%base
def is_divide(base:int,number:int) -> bool:
    return not base%number
center=centre
heart_symbol='❤'
multiply_symbol='×'
divide_symbol='÷'
empty_square_symbol='□'
empty_circle_symbol='○'
full_square_symbol='■'
full_circle_symbol='●'
dotted_empty_circle_symbol='◌'
fundamental_symbols_list=['+','-',multiply_symbol,divide_symbol]
class chart:
    def __init__(self,a):
        self.a=a
        self.inform=[['    ' for _ in range(self.a)] for _ in range(self.a)]
        self.state=max([max([len(i) for i in j]) for j in self.inform]) // 4 
        if self.state>=2:
            self.row_num=self.state//2 
        else:
            self.row_num=1
    def __str__(self) -> str:
        return_chart=''''''
        for i in self.inform:
            return_chart+=f'''{('+'+'-'*4*self.state)*self.a}+\n'''
            for enu,_ in enumerate(range(self.state),1):
                for j in i:
                    j=str(j)
                    qwert=4*self.state
                    return_chart+=f'|{centre(j,qwert)}' if enu==self.row_num else ('|'+' '*qwert)
                return_chart+='|\n'
        return_chart+=f'''{('+'+'-'*4*self.state)*self.a}+'''
        return return_chart
    def change(self,position,inform):
        inform=str(inform)
        (self.inform[position[1]-1])[position[0]-1]=inform
        self.state=max([max([len(i) for i in j]) for j in self.inform]) // 4 
        self.row_num=self.state//2 
        if self.state>=2:
            self.row_num=self.state//2 
        else:
            self.row_num=1
def decimal_part(decimal:float|str) -> int:
    return int(f'{decimal}'.split('.')[-1])
def integer_part(decimal:float|str) -> int:
    return int(f'{decimal}'.split('.')[0])
def round_by_four_five(decimal:float,digit:int=0) -> float|int:
    str_decim=f'{decimal}'
    look_digit=digit+1
    ne=len(f'{decimal_part(decimal)}')
    if ne<digit:
        raise ValueError
    elif ne==digit:
        return decimal
    partofdecimal=f'{decimal_part(decimal)}'
    lookint=int(partofdecimal[digit])
    pod=partofdecimal[:digit:]
    if lookint<=4:
        return eval(f'{integer_part(decimal)}.{pod}')
    else:
        a=eval(f'{integer_part(decimal)}.{eval(pod)+1}')
        return a
def reduct(number_1:int,number_2:int) -> list[int,int]:
    same=greatest_common_divisor(number_1,number_2)
    return [number_1//same,number_2//2]
def multiple_in_range(number:int,start_to_find:int,end_to_find:int,include_end:bool=True) -> list[int]:
    rtl=[]
    for i in range(start_to_find,end_to_find+1 if include_end else end_to_find):
        if is_multiple(number,i):
            rtl.append(i)
    return rtl
def multiples_in_range(numbers:list,start_to_find:int,end_to_find:int,include_end:bool=True) -> list[int]:
    rt={*()}
    for i in numbers:
        for j in multiple_in_range(i,start_to_find,end_to_find,include_end):
            rt.add(j)
    return list(rt)
def only_multiples_in_range(numbers:list,start_to_find:int,end_to_find:int,include_end:bool=True) -> list[int]:
    rt=[]
    rang=range(start_to_find,end_to_find+1 if include_end else end_to_find)
    for num in rang:
        if is_only_prime_factor(num,numbers):
            rt.append(num)
    return rt
