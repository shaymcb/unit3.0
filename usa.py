#Shaylee McBride
#15Feb2018
#usa.py

from ggame import *

red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
y=int(input('Enter flag height: ')) #y is flag height, used as scaling factor in like everything so I made it one letter
x = y/80 #scale factor for stars, probably shouldn't have called it x but whatever
distx = (0.063*y-4.9*x/2)/y #x distance between stars, initial position is measured from center but python measures from top left so had to adjust that
disty = (0.054*y-5*x/2)/y #y distance between stars
blueWidth = 0.76 * y
blueHeight = 7/13 * y
stripeWidth = 1.9 * y
stripeHeight = y / 13

outline = LineStyle(0,white)

star = PolygonAsset([(x*.073,x*2.417),(x*1.927,x*2.417),(x*2.5,x*0.383),(x*3.073,x*2.417),(x*4.927,x*2.417),(x*3.427,x*3.237),(x*4,x*5),(x*2.5,x*3.91),(x*1,x*5),(x*1.573,x*3.237)],outline,white)
blueRectangle = RectangleAsset(blueWidth,blueHeight,outline,blue)
redRectangle = RectangleAsset(stripeWidth,y,outline,red)
whiteStripe = RectangleAsset(stripeWidth,stripeHeight,outline,white)
background = RectangleAsset(1000,1000,outline,black)

Sprite(background)

#stripes
Sprite(redRectangle)
for i in range(0,6):
    Sprite(whiteStripe,(0,(1/13+2*i/13)*y))

#stars
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
