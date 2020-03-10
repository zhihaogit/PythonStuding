# 使用 Python 生成类似于下图中的字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, sys, os
basePath = sys.path[0]
path = os.path.join(basePath, 'DejaVuSansMono.ttf')

image = Image.new('RGB', (50 * 4, 50), (255, 255, 255))
font = ImageFont.truetype(path, 24)
draw = ImageDraw.Draw(image)

def randColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def randColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def randChar():
    return chr(random.randint(65, 90))

for x in range(50 * 4):
    for y in range(50):
        draw.point((x, y), randColor())

for x in range(4):
    draw.text((50 * x + 10, 10), randChar(), randColor2(), font)

image = image.filter(ImageFilter.BLUR)
image.save('result.jpg')
image.show()