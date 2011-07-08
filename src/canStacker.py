from pyx import *
from math import *
from geom import *

unit.set(defaultunit="mm")

debug =1

# Outer dimensions of the cabinet
outerHeight=178
outerWidth=111+6
outerDepth=390

canHeight=120
canDiam=80

boardThickness = 3
margin=7

cut = [style.linewidth(0.02), color.rgb.red]
raster_engrave= [style.linewidth(0.02), color.rgb.black]
vector_engrave= [style.linewidth(0.02), color.rgb.blue]


#create the picture
c = canvas.canvas()

# bounding Box
shape = rect(0,0, outerDepth, outerHeight)
c.stroke(shape, cut)

# Engrave top shelf outline, no slope
topShelfLeft = float(canDiam+boardThickness+margin)
topShelfRight = float(outerDepth -20)
topShelfTop = float(outerHeight-canDiam)
topShelfBottom = float(topShelfTop-boardThickness)
if debug:
    shape = rect(topShelfLeft, topShelfTop,
                 topShelfRight, topShelfBottom)
    c.stroke(shape, vector_engrave)
# engrave the tabs for the top shelf
topShelfNumTabs = float(5)
topShelfTabLength=(topShelfRight-topShelfLeft)/(2*topShelfNumTabs-1)
for i in range(int(topShelfNumTabs)):
    tabLeft = topShelfLeft+ (i*2)*topShelfTabLength
    tabRight = tabLeft+topShelfTabLength
    shape = rect(tabLeft, topShelfTop,
                 tabRight, topShelfBottom)
    c.stroke(shape, cut)

# Engrave bottom shelf outline, no slope
bottomShelfLeft = float(canDiam+boardThickness+margin)
bottomShelfRight = float(outerDepth - 20)
bottomShelfTop = float(outerHeight-canDiam-boardThickness-canDiam)
bottomShelfBottom =float(bottomShelfTop-boardThickness)
shape = rect(bottomShelfLeft, 
             bottomShelfTop, 
             bottomShelfRight, 
             bottomShelfBottom)
c.stroke(shape, vector_engrave)

bottomShelfNumTabs = float(5)
bottomShelfTabLength=(bottomShelfRight-bottomShelfLeft)/(2*bottomShelfNumTabs-1)
for i in range(int(bottomShelfNumTabs)):
    tabLeft = bottomShelfLeft+ (i*2)*bottomShelfTabLength
    tabRight = tabLeft+bottomShelfTabLength
    shape = rect(tabLeft, bottomShelfTop,
                 tabRight, bottomShelfBottom)
    c.stroke(shape, cut)


#Engrave the inner arc
shape= path.path(path.arc(canDiam+boardThickness+margin, 
                outerHeight-canDiam-boardThickness,
                canDiam,
                180, 
                270))
c.stroke(shape, vector_engrave)

#Engrave the outer arc
shape= path.path(path.arc(canDiam+boardThickness+margin, 
                outerHeight-canDiam-boardThickness,
                canDiam+boardThickness,
                180, 
                270))
c.stroke(shape, vector_engrave)
                
#Engrave the top of the lower shelf
shape = rect(margin, outerHeight-(canDiam/2), 
             margin+boardThickness, outerHeight-canDiam-boardThickness)
c.stroke(shape, vector_engrave)

# Cut tabs for the vertical piece of the lower shelf

top = float(outerHeight-(canDiam/2))
bottom = float(outerHeight-canDiam-boardThickness)

tabLength=(top-bottom)/3
# top cut
shape = rect(margin, top, 
             margin+boardThickness, top-tabLength)
c.stroke(shape, cut)
# bottom cut
shape = rect(margin, bottom+tabLength, 
             margin+boardThickness, bottom)
c.stroke(shape, cut)

if debug:
    # Show a border for debug
    pass
    

#c.writePDFfile("output/Side")
c.writeEPSfile("output/Side")

