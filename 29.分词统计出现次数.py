import jieba
with open('文件.txt','r',encoding='utf-8') as file:
    s=file.read()
print(s)
lst=jieba.lcut(s)
print(lst)