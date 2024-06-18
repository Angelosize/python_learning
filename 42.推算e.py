from useful_tools import time
n=1
lst=[]
while True:
    e=(1+1/n)**n
    # print(e)
    lst.append(e)
    if len(lst)>=2:
        if lst[-1]==lst[-2]:
            print(e)
            break
    n+=1