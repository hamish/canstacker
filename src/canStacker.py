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

### Cut the actual top shelf
shelfCanvas = canvas.canvas()
topshelfLength= outerDepth - (canDiam+boardThickness+margin)
shape = rect(0,0, topshelfLength, outerWidth)
shelfCanvas.stroke(shape, cut)

for i in range(int(topShelfNumTabs-1)):
    tabLeft = ((i)*2)*topShelfTabLength+topShelfTabLength
    tabRight = tabLeft+topShelfTabLength
    shape = rect(tabLeft, boardThickness,
                 tabRight, 0)
    shelfCanvas.stroke(shape, cut)
    shape = rect(tabLeft, outerWidth,
                 tabRight, outerWidth - boardThickness)
    shelfCanvas.stroke(shape, cut)
tabLeft = ((topShelfNumTabs)*2-1)*topShelfTabLength
tabRight = topshelfLength

shape = rect(tabLeft, boardThickness,
                 tabRight, 0)
shelfCanvas.stroke(shape, cut)
shape = rect(tabLeft, outerWidth,
                 tabRight, outerWidth - boardThickness)
shelfCanvas.stroke(shape, cut)


shelfCanvas.writePDFfile("output/TopShelf")


# Engrave bottom shelf outline, no slope
bottomShelfLeft = float(canDiam+boardThickness+margin)
bottomShelfRight = float(outerDepth - 20)
bottomShelfTop = float(margin+boardThickness)
#bottomShelfTop = float(outerHeight-canDiam-boardThickness-canDiam)
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
arcCenterX= canDiam+boardThickness+margin
arcCenterY=bottomShelfTop + canDiam

shape= path.path(path.arc(arcCenterX, 
                arcCenterY,
                canDiam,
                180, 
                270))
c.stroke(shape, vector_engrave)

#Engrave the outer arc
shape= path.path(path.arc(arcCenterX, 
                arcCenterY,
                canDiam+boardThickness,
                180, 
                270))
c.stroke(shape, vector_engrave)
                
#Engrave the top of the lower shelf
vertTop = float(outerHeight-(canDiam/2))
#vertBottom = float(outerHeight-canDiam-boardThickness)
vertBottom= float(margin+boardThickness+canDiam)
shape = rect(margin, vertTop, 
             margin+boardThickness, vertBottom)
c.stroke(shape, vector_engrave)

# Cut tabs for the vertical piece of the lower shelf
vertTabLength=(vertTop-vertBottom)/3
# top cut
shape = rect(margin, vertTop, 
             margin+boardThickness, vertTop-vertTabLength)
c.stroke(shape, cut)
# bottom cut
shape = rect(margin, vertBottom+vertTabLength, 
             margin+boardThickness, vertBottom)
c.stroke(shape, cut)

c.writePDFfile("output/Side")
#c.writeEPSfile("output/Side")

### Cut the actual bottom shelf
backshelfCanvas = canvas.canvas()
#backVert = canDiam/2+boardThickness
backVert = vertTop - vertBottom

backArc = 2*pi*canDiam/4
backHorizontal=outerDepth - (canDiam+boardThickness+margin) 
backshelfLength= backVert+backArc+backHorizontal
shape = rect(0,0, backshelfLength, outerWidth)
backshelfCanvas.stroke(shape, cut)

for i in range(int(topShelfNumTabs-1)):
    tabLeft = backVert+backArc+((i)*2)*topShelfTabLength+topShelfTabLength
    tabRight = tabLeft+topShelfTabLength
    shape = rect(tabLeft, boardThickness,
                 tabRight, 0)
    backshelfCanvas.stroke(shape, cut)
    shape = rect(tabLeft, outerWidth,
                 tabRight, outerWidth - boardThickness)
    backshelfCanvas.stroke(shape, cut)
tabLeft = backVert+backArc+((topShelfNumTabs)*2-1)*topShelfTabLength
tabRight = backshelfLength

shape = rect(tabLeft, boardThickness,
                 tabRight, 0)
backshelfCanvas.stroke(shape, cut)
shape = rect(tabLeft, outerWidth,
                 tabRight, outerWidth - boardThickness)
backshelfCanvas.stroke(shape, cut)
## vetical tabs
shape = rect(vertTabLength, boardThickness,
                 vertTabLength*2, 0)
backshelfCanvas.stroke(shape, cut)

shape = rect(vertTabLength, outerWidth,
                 vertTabLength*2, outerWidth - boardThickness)
backshelfCanvas.stroke(shape, cut)

# cut out the arc
shape = rect(backVert, boardThickness,
             backVert+backArc, 0)
backshelfCanvas.stroke(shape, cut)

shape = rect(backVert, outerWidth,
             backVert+backArc, outerWidth - boardThickness)
backshelfCanvas.stroke(shape, cut)



backshelfCanvas.writePDFfile("output/BottomShelf")
