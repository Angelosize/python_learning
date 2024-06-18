import requests,re
url='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
resp=requests.get(url)
with open('python_files\logo.jpg','wb')as file:
    file.write(resp.content)
