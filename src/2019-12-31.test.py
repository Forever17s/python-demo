# encoding:utf-8
"""
author: wgc
version: 0.9
"""
from PIL import Image, ImageFilter

# 剪裁图像
# def main():
#     image = Image.open('./tests/telnet.png')
#     rect = 80, 20, 300, 360
#     image.crop(rect).show()

# 生成缩略图
# def main():
#     image = Image.open('./tests/telnet.png')
#     size = 128, 128
#     image.thumbnail(size)
#     image.show()

# 缩放和粘贴图像
# def main():
#     imageA = Image.open('./tests/secret.png')
#     imageB = Image.open('./tests/telnet.png')
#     rect = 80, 20, 310, 360
#     guido_head = imageB.crop(rect)
#     width, height = guido_head.size
#     imageA.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))),
#                  (400, 200))
#     imageA.show()

# 旋转和翻转
# def main():
#     image = Image.open('./tests/secret.png')
#     image.rotate(180).show()
#     image.transpose(Image.FLIP_LEFT_RIGHT).show()

# 操作像素
# def main():
#     image = Image.open('./tests/secret.png')
#     for x in range(100, 200):
#         for y in range(20, 300):
#             image.putpixel((x, y), (128, 128, 128))

#     image.show()


# 滤镜效果
def main():
    image = Image.open('./tests/secret.png')
    image.filter(ImageFilter.CONTOUR).show()


if __name__ == '__main__':
    main()
