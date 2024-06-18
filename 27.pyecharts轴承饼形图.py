#python_files\我爱轴承.xlsx
from pyecharts import options as opts
from pyecharts.charts import Pie,Line
from pyecharts.faker import Faker
lastweekzh=eval(input("上个月原有轴承多少件:"))
thisweekzh=eval(input("这个月新进轴承多少件:"))
getoutzh=eval(input("取走了轴承多少件:"))
lastweekdj=eval(input("上个月原有电机多少件:"))
thisweekdj=eval(input("这个月新进电机多少件:"))
getoutdj=eval(input("取走了电机多少件:"))
lst=[
    ['类别','原有库存件数','本月新进件数','本月支出件数','本月剩余件数'],
    ['轴承',lastweekzh,thisweekzh,getoutzh,lastweekzh+thisweekzh-getoutzh],
    ['电机',lastweekdj,thisweekdj,getoutdj,lastweekdj+thisweekdj-getoutdj]
]

c = (
    Pie()
    .add("", [['轴承',lastweekzh],['电机',lastweekdj]])
    .set_global_opts(title_opts=opts.TitleOpts(title="上个月原有轴承与电机的数量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("python_files\lastweekzh.html")
)

c = (
    Pie()
    .add("", [['轴承',thisweekzh],['电机',thisweekdj]])
    .set_global_opts(title_opts=opts.TitleOpts(title="这个月新进轴承与电机的数量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("python_files\thisweekzh.html")
)
c = (
    Pie()
    .add("", [['轴承',getoutzh],['电机',getoutdj]])
    .set_global_opts(title_opts=opts.TitleOpts(title="这个月支出轴承与电机的数量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("python_files\getoutzh.html")
)
c = (
    Pie()
    .add("", [['轴承',lastweekzh+thisweekzh-getoutzh],['电机',lastweekdj+thisweekdj-getoutdj]])
    .set_global_opts(title_opts=opts.TitleOpts(title="这个月剩余轴承与电机的数量"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("python_files\lastzh.html")
)

c = (
    Line()
    .add_xaxis(['上个月剩余库存','这个月剩余库存'])
    .add_yaxis("轴承",[lastweekzh,lastweekzh+thisweekzh-getoutzh])
    .add_yaxis("电机", [lastweekdj,lastweekdj+thisweekdj-getoutdj])
    .set_global_opts(title_opts=opts.TitleOpts(title="轴承与电机上个月剩余与这个月剩余的对比图"))
    .render("python_files\comparezh.html")
)
