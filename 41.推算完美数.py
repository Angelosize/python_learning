from useful_tools import is_prime,find_factor
from typing import List
def find_perfect_number(start_number:int=1,number_to :int= 6,include_number_to:bool=True) -> list[int]: # include number_to
    '''
    include number_to
    '''
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
    for ij in find_factor(number):
        if ij!=number:
            sums+=ij
    if sums==number:
        return True
    return False

print(find_perfect_number(1,1_0000_0000_0000_0000_0000_0000))