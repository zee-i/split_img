from PIL import Image
import os

#需要处理的图片所在的目录
path = 'X:\\xxx\\xxx'

path_list = os.listdir(path)

print(path_list)

n = 0
for i in path_list:

    #为了方便给图片命名
    n = n + 1
  
    f = open(os.path.join(path,i), 'rb')
    img = Image.open(f)
    w = img.width
    h = img.height
    
    print('正在处理图片', i, '宽', w, '长' , h)

    #想要截取的左上角和右下角的坐标
    box_r = (w * 0.5, 0, w, h)
    box_l = (0, 0, w * 0.5, h)
        
    img_r = img.crop(box_r)
    print('正在截取左边')
    img_r.save(str((n*2-1)) + '.jpg' )
    
    img_l = img.crop(box_l)
    print('正在截取右边')
    img_l.save(str((n*2)) + '.jpg')

print('完')
