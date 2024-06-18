dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','19:19','00:59'],
    'G2031':['北京南-天津南','18:35','19:09','00:34']
}
print('今日车次表'.center(63,'-'))
print('车次   出发站-到达站\t\t出发时间\t到达时间\t历时时长')
for key in dict_ticket.keys():
    print(key,end='  ')
    for item in dict_ticket.get(key):
        print(item,end='\t\t')
    print()
n=input('请输入要购买的车次')
info=dict_ticket.get(n,'车次不存在')
if info!='车次不存在':
    per=input('请输入乘车人，如果是多位乘车人使用逗号分隔:')
    s_t=info[0]+' '+info[1]+'开,'
    print('您已购买了'+n+' '+s_t+'请'+per+'尽快换取纸质车票[铁路客服]')
else:
    print('对不起，您选择的车次不存在')
    
print('Made by Angelo_size')