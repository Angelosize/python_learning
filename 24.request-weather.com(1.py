import requests,re
url='http://www.weather.com.cn/weather1d/101010100.shtml'
resp=requests.get(url)
resp.encoding='utf-8'
print()
city=re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',resp.text)
weather=re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',resp.text)
temp=re.findall('<span class="wd">(.*)</span>',resp.text)
zs=re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',resp.text)
#print(city,'\n',weather,'\n',temp,'\n',zs,sep='')
lst=[]
for a,b,c,d in zip(city,weather,temp,zs):
    lst.append([a,b,c,d])
for item in lst:
    for i in item:
        print(i,end='\t')
    print()