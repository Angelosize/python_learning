import time
from math import log
def no_float(a_float:float) -> int:
    return int(str(a_float).split('.')[0])
pi=0
try_number=0
while True:
    pi+=1/pow(16,try_number) * (4/(8*try_number+1) - 2/(8*try_number+4) - 1/(8*try_number+5) - 1/(8*try_number+6))    
    if try_number<10:
        try_number+=1
    else:
        try_number+=no_float(log(try_number,10))
    print(pi)
    time.sleep(0.8)
    


