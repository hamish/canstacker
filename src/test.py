from pyx import *
from math import *
from geom import *

unit.set(defaultunit="mm")

cut = [style.linewidth(0.02), color.rgb.red]
raster_engrave= [style.linewidth(0.02), color.rgb.black]
vector_engrave= [style.linewidth(0.02), color.rgb.blue]


#create the picture
c = canvas.canvas()

# bounding Box
rectangle=RotatableRectangle(XDistance=30, YDistance=40, angle=10)

shape = rectanglePath(rectangle)
c.stroke(shape, cut)

c.writePDFfile("output/test")
#c.writeEPSfile("output/test")
