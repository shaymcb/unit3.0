#Shaylee McBride
#15Feb2018
#usa.py - makes a usa flag

from ggame import *

#colors & outline
red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
outline = LineStyle(0,white)

#dimensions
h=int(input('Enter flag height (ex. 500): ')) #h is flag height, used as scaling factor in like everything so I made it one letter
x = h/80 #scale factor for stars, probably shouldn't have called it x but whatever
distx = (0.063*h-4.9*x/2)/h #x distance between stars, initial position is measured from center but python measures from top left so had to adjust that
disty = (0.054*h-5*x/2)/h #y distance between stars, same deal with initial position
blueWidth = 0.76 * h
blueHeight = 7/13 * h
stripeWidth = 1.9 * h
stripeHeight = h / 13

#shapes
star = PolygonAsset([(x*.073,x*2.417),(x*1.927,x*2.417),(x*2.5,x*0.383),(x*3.073,x*2.417),(x*4.927,x*2.417),(x*3.427,x*3.237),(x*4,x*5),(x*2.5,x*3.91),(x*1,x*5),(x*1.573,x*3.237)],outline,white)
blueRectangle = RectangleAsset(blueWidth,blueHeight,outline,blue)
redRectangle = RectangleAsset(stripeWidth,h,outline,red)
whiteStripe = RectangleAsset(stripeWidth,stripeHeight,outline,white)

#stripes
Sprite(redRectangle)
for i in range(6):
    Sprite(whiteStripe,(0,(1/13+2*i/13)*h))

#stars
Sprite(blueRectangle)
for j in range(5):
    for i in range(6):
        Sprite(star,(distx*h,disty*h))
        if i != 5 and j != 4:
            Sprite(star,(.063*h+distx*h,.054*h+disty*h))
        distx +=.126
    disty += .108
    distx = 0.032

App().run()
