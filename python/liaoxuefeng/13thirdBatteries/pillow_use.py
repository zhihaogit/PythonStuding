# PIL(Python Imaging Library)，事实上的图像处理标准库，仅支持到 2.7
# PIL的兼容版本，Pillow

# 安装 Pillow
# pip install pillow

# 缩放图像
from PIL import Image

# 打开一个 jpg图像，当前路径
im = Image.open('test.jpg')
# 获得图像尺寸
w, h = im.size
print ('Original image size: %sx%s' % (w, h))
# 缩放到 50%
im.thumbnail(w//2, h//2)
print ('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用 jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')


# 模糊效果
from PIL import Image, ImageFilter
im = Image.open('test.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')


# ImageDraw，绘图方法
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母：
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1：
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2：
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建 Font对象
# 可以根据操作系统提供绝对路径
font = ImageFont.truetype('Arial.ttf', 36)
# 创建 Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor())
# 输出文字
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor2())
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')


















































