# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果
import sys
from PIL import Image, ImageDraw, ImageFont

def addNum(image):
    draw = ImageDraw.Draw(image)
    myFont = ImageFont.truetype('/System/Library/Fonts/SFCompactDisplay.ttf', 30)
    # IOError: cannot open resource
    # 这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径
    fillcolor = '#ff0000'
    width, height = image.size
    draw.text((width - 40, 0), '99', font = myFont, fill = fillcolor)
    image.save('result.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    absolutePath = sys.argv[1]
    # 找到命令行中输入的图片的绝对路径
    img = Image.open(absolutePath)
    addNum(img)