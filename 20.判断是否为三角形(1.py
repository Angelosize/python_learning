try:
    a=float(input('请输入三角形第一条边的边长:'))
    b=float(input('请输入三角形第二条边的边长:'))
    c=float(input('请输入三角形第三条边的边长:'))
    if a+b>c and a+c>b and b+c>a:
        print(f'三条边的边长分别为{a},{b},{c},它们能围成一个三角形')
    else:
        raise Exception(f'三条边的边长分别为{a},{b},{c},它们无法围成三角形')
except ValueError:
    print('边长输入有误')
except Exception as i:
    print(i)
print('Made by Angelo_size')