import time
lst=[]
cart=[]
prices=[]
sum_prices=[]
newct=[]
mon=0
a=eval(input('请输入要入库的商品数量:'))
for i in range(a):
    goods=input('请输入商品的四位数编号和商品的名称进行商品入库,每次只能输入一件商品:')
    lst.append(goods)
    price=eval(input('它的价格是(以元为单位):'))
    prices.append(price)
print('-'*50)
print('已入库商品:')
for it in lst:
    print(it)
while True:
    flag=False
    num=input('请输入要购买的商品的四位数编号(输入q视为退出):')
    if num!='q':
        thing_numbers=eval(input('请输入要购买的商品个数:'))
    for index,it in enumerate(lst):
        if num==it[0:4]:
            flag=True
            for i in range(thing_numbers):
                cart.append(it)
                sum_prices.append(prices[index])
            print('商品已成功添加到购物车')
            break
    if not flag and num!='q':
        print('商品不存在!')
    if num=='q':
        print('已退出,正在结算')
        time.sleep(2)
        break
print('-'*50)
for i in cart:
    
    c=cart.count(i)
    newct.append(f'{c}件{i[4::]}')
    for i1 in range(c):
        cart.remove(i)








print('您购物车中已选择的商品为:')
newct.reverse()
for it in newct:
    print(it)
for y in sum_prices:
    mon+=y
print(f'一共用了{mon}元')
print('Made by Angelo_size')