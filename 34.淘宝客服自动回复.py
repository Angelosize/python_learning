def find_answer(question):
    with open('python_files/replay.txt','r',encoding='utf-8') as file:
        while True:
            line=file.readline()
            if line=='':
                break
            keyword=line.split('|')[0]
            reply=line.split('|')[1]
            if keyword in question:
                return reply
    return None
if __name__=='__main__':
    question=input('请问有什么问题(输入"退出"以退出):')
    while True:
        if question=='退出':
            print('退出成功')
            break
        else:
            reply=find_answer(question)
            if reply==None:
                question=input('问题不支持,请换个关于订单,物流,支付和账户方面的问题(输入"退出"以退出):')
            else:
                print(reply)
                question=input('请问有什么问题(输入"退出"以退出):')
