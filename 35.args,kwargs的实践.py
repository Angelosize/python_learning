
class Package:
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
    def toppings(self):
        print('toppings:')
        a=1
        for i in self.args:
            print(f'-  {a}:{i}')
            a+=1
    def details(self):
        print('details:')
        a=1
        for i,v in self.kwargs.items():
            print(f'-  {a}:{i}--->{v}')
            a+=1
    def show(self):
        print('toppings:')
        a=1
        for i in self.args:
            print(f'-  {a}:{i}')
            a+=1
        print('details:')
        a=1
        for i,v in self.kwargs.items():
            print(f'-  {a}:{i}--->{v}')
            a+=1
    def __iadd__(self,another_package):
        a=self.args+another_package.args
        values=[]
        keys=[]
        b=self.kwargs
        c=another_package.kwargs
        for i in b.values():
            values.append(i)
        for i in c.values():
            values.append(i)
        for i in b.keys():
            keys.append(i)
        for i in c.keys():
            keys.append(i)
        e={i:j for i,j in zip(keys,values)}
        self.args=a
        self.kwargs=e
        return self
    

a=Package('a','ad',cheese=True,ss='a')
# a.toppings()
# a.details()
# a.show()
b=Package(1,12,2,2,1,2,1,cdc=True)
# c.show()
# d=a+c;d.show()
a+=b;a.show()
print('-'*80)

