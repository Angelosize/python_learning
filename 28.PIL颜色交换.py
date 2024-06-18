from PIL import Image
im=Image.open('logo.jpg')
print(im)
r,g,b,a=im.split()
# print(r,g,b)
om=Image.merge(mode='RGBA',bands=(b,g,a,r))
om.save('python_files\new_google.png')