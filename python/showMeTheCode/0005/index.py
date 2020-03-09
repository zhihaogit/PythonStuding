# 有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
import os
from PIL import Image

path = 'imageDir'
resultPath = 'resultDir/'

def pathHandler(f):
    return os.path.join(path, f);

for f in os.listdir(path):
    img = Image.open(pathHandler(f))
    w, h = img.size
    w = 1136 if (w > 1136) else w
    h = 640 if (h > 640) else h
    # Image.ANTIALIAS 滤镜缩放效果
    img = img.resize((w, h), Image.ANTIALIAS)
    img.save(resultPath + f)

