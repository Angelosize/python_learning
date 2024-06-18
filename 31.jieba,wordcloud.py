import jieba
from wordcloud import WordCloud
with open('python_files\w1.txt','r',encoding='utf-8') as file:
    s=file.read()
lst=jieba.lcut(s)
print(lst)