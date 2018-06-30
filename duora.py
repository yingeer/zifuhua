import argparse
from PIL import Image


#命令行参数处理
parser=argparse.ArgumentParser()

parser.add_argument("file")
parser.add_argument("-o","--output")
parser.add_argument("--width",type=int, default=80)
parser.add_argument("--height", type=int, default=80)

argument=parser.parse_args()
#获取参数
IMG=argument.file
HEIGHT=argument.height
WIDTH=argument.width
OUTPUT=argument.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
""":parameter 
r g b alpha
return: 对应的字符"""

def get_char(r, g, b, alpha=256):
    #如果没有像素点, 返回空格
    if alpha==0:
        return " "
    length=len(ascii_char)
    unit=(256.0+1)/length
    #得到一个像素点的灰度直
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    image=Image.open(IMG)
    image=image.resize((WIDTH, HEIGHT), Image.NEAREST)

    txt=""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+=get_char(*image.getpixel((j, i)))
        txt+="\n"

    print(txt)

    #将字符画输入到文件里
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)

    else:
        with open ('duora.txt ', 'w') as f:
            f.write(txt)
