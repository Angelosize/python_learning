# 猜数游戏
import random

# 默认生成的数字
num = random.randint(1, 100)
# 记录猜数的次数
count = 1
#先猜测一次
guess = random.randint(1, 100)
# 初始化最大值，最小值
min = 1
max = 100


# 取两个数字的中间数字(二分猜数生成器)
def fun(min, max):
    # 向下取整数
    middle = int((min + max) / 2)
    return middle


while True:
    print(f'我猜是:{guess}')
    diff = guess - num
    if diff == 0:
        print('恭喜你猜中了')
        break
    else:
        count += 1
        if diff > 0:
            print('猜大了')
            max = guess
            guess = fun(min, max)
        else:
            print('猜小了')
            min = guess
            guess = fun(min, max)

print(f'一共猜了{count}次')
print('Made by Angelo_size')