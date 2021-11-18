from PIL import Image, ImageDraw, ImageFilter
import loader

def render(num):
    line_width=10
    padding=40
    icon_width=256
    totalwidth=6*padding+3*icon_width+2*line_width
    image = Image.new("RGB", (totalwidth, totalwidth), (234, 223, 202))
    image.paste(loader.tictacX, mask=loader.tictacX)
    image.save("test.png", "PNG")
    return
    state=[]
    while num>0:
        state.append(num%3)
        num=int(num/3)
        image.paste(loader.tictacX, (), mask=loader.tictacX)
render(5)