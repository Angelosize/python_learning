lst=[
    ['01','电风扇','美的',500],
    ['02','洗衣机','TCL',1000],
    ['03','微波炉','东芝',400]
]
print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
    for item2 in item:
        print(item2,end='\t\t')
    print()
for item in lst:
    item[0]='0000'+item[0]
    item[3]='￥{0:.2f}'.format(item[3])
print('-'*59)
print('编号\t\t名称\t\t品牌\t\t单价')
for item in lst:
    for item2 in item:
        print(item2,end='\t\t')
    print()
print('Made by Angelo_size')