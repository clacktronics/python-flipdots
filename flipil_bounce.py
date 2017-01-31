from PIL import Image, ImageDraw
import numpy
from flipil import flipil


if __name__ == "__main__":



    from time import sleep
    from PIL import ImageDraw
    from random import randrange
    refresh = [0x80,0x82,0x8F]

    panel1 = flipil("alfa_zeta", [28, 7], [[8,16,24],[7,15,23],[6,14,22],[5,13,21],[4,12,20],[3,11,19],[2,10,18],[1,9,17]], init_color = 0, reverse_panel=False)
    panel1.set_port('/dev/ttyAMA0', 57600)

    def sim(image):
        dot = 8
        gap = 5
        img = Image.new("L", (image.size[0]*(dot+gap),image.size[1]*(dot+gap)), color=50)
        drw = ImageDraw.Draw(img)
        for yn, y in enumerate(numpy.array(image).tolist()):
            for xn, x in enumerate(y):
                xpos = xn*(dot+gap)
                ypos = yn*(dot+gap)
                drw.ellipse((xpos, ypos, xpos+dot, ypos+dot), fill=x )
        return img

	
 
    draw = ImageDraw.Draw(panel1)

    size = 32
    dir_x = 1
    dir_y = 1
    x = 1
    y = 1

    while True:
        print x, y

	if x+size+2 > panel1.width or x < 1:
            dir_x *= -1
	if y+size+2 > panel1.height or y < 1:
            dir_y *= -1

        x += dir_x
        y += dir_y

        panel1.clear()
        draw = ImageDraw.Draw(panel1)
#        draw.text((0,20), "BEN!", fill=1)
        draw.ellipse((x,y,x+size,y+size), outline=1, fill=0)

        panel1._translate()
        panel1.send()


