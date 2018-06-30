from PIL import Image, ImageDraw, ImageFont
from random import *


"""获得随机验证码"""
class GetYanzhengma:
    def __init__(self, mode="RGB", height=50, width=200, color="red", size=40):
        # 创建image对象
        self.height = height
        self.width = width
        self.img = Image.new(mode, (self.width, self.height), color)
        # 创建一个画笔对象
        self.draw = ImageDraw.Draw(im=self.img)
        # 字体对象
        self.size = size
        self.font = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK.ttc", self.size)

    # 获得随机颜色
    def get_color(self):
        c1 = randint(0, 255)
        c2 = randint(0, 255)
        c3 = randint(0, 255)
        return (c1, c2, c3)

    # 获得单个随机字符
    def get_char(self):
        lower_char = chr(randint(97, 123));
        upper_char = chr(randint(65, 90));
        ran_num = str(randint(0, 9))
        random_char = choice([lower_char, upper_char, ran_num])
        return random_char

    # 获得随机字符串
    def get_random_string(self, string="", num=5):

        for char in range(num):
            string += self.get_char() + "  "
        return string

    # 画线
    def draw_line(self, num=5):

        for i in range(num):
            x1 = randint(0, self.width);
            y1 = randint(0, self.height)
            x2 = randint(0, self.width);
            y2 = randint(0, self.height)
            self.draw.line((x1, y1, x2, y2), fill=self.get_color())

    # 画上验证字符串
    def draw_string(self):

        self.draw.text((20, 0), self.get_random_string(), self.get_color(), font=self.font)

    # 画点
    def draw_dots(self, num=30):
        for i in range(num):
            self.draw.point([randint(0, self.width), randint(0, self.height)], fill=self.get_color())
            # 画弯点
            x = randint(0, self.width)
            y = randint(0, self.height)
            self.draw.arc((x, y, x + 4, y + 4), 0, 90, fill=self.get_color())


if __name__ == '__main__':
    yanzheng = GetYanzhengma()
    yanzheng.get_color()
    yanzheng.get_char()
    yanzheng.get_random_string()
    yanzheng.draw_line()
    yanzheng.draw_string()

    with open('images/yanzheng.png', 'wb') as f:
        yanzheng.img.save(f)
