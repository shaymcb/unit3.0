#Shaylee McBride
#15Feb2018
#usa.py

from ggame import *

red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)
x = 5
y=400
distx = 0.032
disty = 0.02
blueWidth = 0.76 * y
blueHeight = 7/13 * y

outline = LineStyle(0,white)

star = PolygonAsset([(x*.073,x*2.417),(x*1.927,x*2.417),(x*2.5,x*0.383),(x*3.073,x*2.427),(x*4.927,x*2.417),(x*3.427,x*3.237),(x*4,x*5),(x*2.5,x*3.91),(x*1,x*5),(x*1.573,x*3.237)],outline,white)
blueRectangle = RectangleAsset(blueWidth,blueHeight,outline,blue)

Sprite(blueRectangle)
for i in range(1,6*5+1):
    Sprite(star,(distx*y,disty*y))
    if i%6 != 0 and i<=6*4:
        Sprite(star,(.063*y+distx*y,.054*y+disty*y))
    distx +=.126
    if i%6 == 0:
        disty += .108
        distx = 0.032

App().run()
