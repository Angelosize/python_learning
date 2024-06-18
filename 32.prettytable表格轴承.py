import prettytable as pt
lastweekzh=eval(input("上个月原有轴承多少件:"))
thisweekzh=eval(input("这个月新进轴承多少件:"))
getoutzh=eval(input("取走了轴承多少件:"))
lastweekdj=eval(input("上个月原有电机多少件:"))
thisweekdj=eval(input("这个月新进电机多少件:"))
getoutdj=eval(input("取走了电机多少件:"))
lst=[['轴承',lastweekzh,thisweekzh,getoutzh,lastweekzh+thisweekzh-getoutzh],['电机',lastweekdj,thisweekdj,getoutdj,lastweekdj+thisweekdj-getoutdj],['合计',lastweekzh+lastweekdj,thisweekzh+thisweekdj,getoutzh+getoutdj,lastweekzh+thisweekzh-getoutzh+lastweekdj+thisweekdj-getoutdj]]

tb=pt.PrettyTable()
tb.field_names=['类别','原有库存件数','本月新进件数','本月支出件数','本月剩余件数']
for item in lst:
    tb.add_row(item)
print(tb)