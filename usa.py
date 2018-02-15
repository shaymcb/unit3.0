#Shaylee McBride
#15Feb2018
#usa.py

from ggame import *

red = Color(0xFF0000,1)
white = Color(0xFFFFFF,1)
blue = Color(0x0000FF,1)

outline = LineStyle(0,white)

star = PolygonAsset([(.073,2.417),(1.927,2.417),(2.5,0.383),(3.073,2.427),(4.927,2.417),(3.427,3.237),(4,5),(2.5,3.91),(1,5),(1.573,3.237)],outline,blue)

Sprite(star)
App().run()
