from coordinates import *
from geom import *

unit.set(defaultunit="mm")

cut = [style.linewidth(0.02), color.rgb.red]
raster_engrave= [style.linewidth(0.02), color.rgb.black]
vector_engrave= [style.linewidth(0.02), color.rgb.blue]
c = canvas.canvas()

rectOrigin=Point(1,1)
rect=RotatableRectangle(origin=rectOrigin, XDistance=-5, YDistance=2)

c.stroke(rectanglePath(rect), vector_engrave)
for tab in tabCuts(rect):
    #print tab.origin
    #print tab.XDistance
    c.stroke(rectanglePath(tab), cut)
    
    
c.writeEPSfile("output/scratch")        
