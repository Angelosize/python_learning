from math import pi
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def get_area(self):
        return self.radius*self.radius*pi
    def get_perimeter(self):
        return 2*self.radius*pi
radius=Circle(eval(input('请输入圆的半径:')))
dig=eval(input('请问您要保留的位数(最大15):'))
per=radius.get_perimeter()
perimeter=round(per,dig)
ar=radius.get_area()
area=round(ar,dig)
print('圆的周长为',perimeter,',圆的面积为',area)