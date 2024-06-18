from useful_tools import CantFindPatternError,get_minus,get_multiple,is_prime,generate_prime_list,turn_float_into_int
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
# find_pattern([1,2,3,4,5])  Exception: [1, 1, 5]
# find_pattern([1,2,4,8,16])  Exception: [2, 2.0, 16]
if __name__=='__main__':
    print(find_pattern([1,2,4,8],5))
    print(find_pattern([1,2,4,7,11]))
    print(find_pattern([1,4,10,19]))
    print(find_pattern([1,2,6,24]))
    print(find_pattern([1,2,8,64]))
    print(find_pattern([2,3,5,7,11]))
    # print(find_pattern([114514,12])):CantFindPatternError: can't find pattern with list which its length is smaller than 4