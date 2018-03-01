#Shaylee McBride
#1March2018
#dotsDemo.py - how to use loops with graphics

from ggame import *

radius = 25

orange = Color(0xFFA600, 1)

dot = CircleAsset(radius,LineStyle(4,Color(0xFF0000,1)),orange)

for j in range(7):
    for i in range(12): #row of dots
      Sprite(dot,(10+(2*radius+20)*i,10+(2*radius+20)*j))

App().run()
