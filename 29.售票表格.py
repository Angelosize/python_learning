import prettytable as pt
try:
    def show_ticket(row_num):
        tb=pt.PrettyTable()
        tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
        for i in range(1,row_num+1):
            lst=[f'第{i}行','有票','有票','有票','有票','有票']
            tb.add_row(lst)
        print(tb)
    def order_ticket(row_num,row,column):
        tb=pt.PrettyTable()
        tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
        for i in range(1,row_num+1):
            if int(row)==i:
                lst=[f'第{i}行','有票','有票','有票','有票','有票']
                lst[int(column)]='已售'
                tb.add_row(lst)
            else:
                lst=[f'第{i}行','有票','有票','有票','有票','有票']
                tb.add_row(lst)
        print(tb)
    if __name__=='__main__':
        row_num=6
        show_ticket(row_num)
        choose=input('请输入您选择的坐席:如4,3表示第4排第3列:')
        row,column=choose.split(',')
        order_ticket(row_num,row,column)
except IndexError:
    print('座位号有误!')
