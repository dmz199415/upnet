from unet import Unet
from PIL import Image
import os
unet=Unet()
path='F:/Unet_test/unet/datasets/JPEGImages'
for files in os.listdir(path):
    print (files)
    try:
        image = Image.open(path+"/"+files)
    except:
        print('open error')
        continue
    else:
        r_image=unet.detect_image(image)
        r_image.save(path+'/'+'aaa'+"/"+files)