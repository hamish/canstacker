from pyx import *
from math import *
from geom import *
from canStacker import *
from coordinates import *
import trig

unit.set(defaultunit="mm")

cut = [style.linewidth(0.02), color.rgb.red]
raster_engrave= [style.linewidth(0.02), color.rgb.black]
vector_engrave= [style.linewidth(0.02), color.rgb.blue]
draw_debug= [style.linewidth.Thick, style.linestyle.dashed, color.rgb.green]

class CanStackerParameters():    
    def __init__(self):
        # At the moment input vars are hard coded, this will change
        self.debug=0
        self.engrave_outline=1
        
        # Master Parameters. All units in mm
        self.boardThickness=float(3)
        self.cabinetDepth=float(390)
        
        # these have some extra room built in so we can create a  
        # space exactly canHeight or canDiameter and assume that 
        # a real can will fit.
        self.canHeight=float(117)
        self.canDiameter=float(80)
        
        self.minFingerDistance=float(30)
        self.minShelfAngle=float(5)
        
        self.margin=float(7)
        self.frontGap=float(1)
        self.backGap=float(10)
        
        self.v2TabVertical=float(1.5)
        self.v2TabHorizontal=float(1.5)
    
    
        self.lowerGateHeight=self.canDiameter/4
        self.upperGateHeight=self.canDiameter/8
        
        ##### Lower Shelf
        self.lsBottomFrontX=self.cabinetDepth-self.margin
        self.lsBottomFrontY=self.margin
        
        self.lsBottomBackX=self.margin+self.boardThickness+self.backGap
        print self.lsBottomFrontX
        print self.lsBottomBackX
        
        self.lsBottomXDistance = self.lsBottomFrontX-self.lsBottomBackX
        self.lsBottomBackY=tan(self.minShelfAngle)*self.lsBottomXDistance
        self.lsLength = trig.getHypotenuse(adjacent=self.lsBottomXDistance, angle=self.minShelfAngle)
        self.lsRectangle=RotatableRectangle(
            XDistance=-1*self.lsLength, 
            YDistance=self.boardThickness,
            origin=Point(self.lsBottomFrontX,self.lsBottomFrontY),
            angle=-1*self.minShelfAngle
                                           )
        
        
        ##### Lower Gate
        lgOrigin=self.lsRectangle.getPosD().clone()
        lgOrigin.slide_xy(0,self.frontGap)
        self.lgRectangle=RotatableRectangle(
            YDistance=self.boardThickness, 
            XDistance=self.lowerGateHeight,
            origin=lgOrigin,
            angle=90 #Defined rotated so that tabs work correctly
                                            )
        
        ###### Top Shelf
        self.tsBottomFront = self.lgRectangle.getPosD().clone()
        self.tsBottomFront.slide_xy(0,self.canDiameter+self.minFingerDistance)
        self.tsBottomBackX=self.margin+self.boardThickness+self.backGap+ self.canDiameter
        self.tsHorizontalDistance = self.tsBottomFront.x-self.tsBottomBackX
        self.tsLength = trig.getHypotenuse(adjacent=self.tsHorizontalDistance, angle=self.minShelfAngle)
        self.tsRectangle=RotatableRectangle(
            XDistance=-1*self.tsLength, 
            YDistance=self.boardThickness,
            origin=self.tsBottomFront,
            angle=self.minShelfAngle
                                           )
        ##### Top Gate
        tgOrigin=self.tsRectangle.getPosD().clone()
        tgOrigin.slide_xy(0,self.frontGap)
        self.tgRectangle=RotatableRectangle(
            YDistance=self.boardThickness, 
            XDistance=self.upperGateHeight,
            origin=tgOrigin, 
            angle=90
                                            )
        self.cabinetHeight = self.tgRectangle.getPosD().y + self.canDiameter
        
        #### Back Wall
        
        bwBottomY=self.lsRectangle.getPosC().y + self.backGap
        bwHeight=self.cabinetHeight - self.backGap - bwBottomY
        bwOrigin = Point(self.margin+self.boardThickness, bwBottomY)
        self.bwRectangle=RotatableRectangle(
            YDistance=self.boardThickness, 
            XDistance=bwHeight,
            origin=bwOrigin,
            angle=90
            )

def strokeTabs(rectangle, canvas, mode, numTabs=3):
    for tab in tabCuts(rectangle, numTabs=numTabs):
        #print tab.origin
        #print tab.XDistance
        canvas.stroke(rectanglePath(tab), mode)
        
        
        #self.v2TabVertical
        #self.v2TabHorizontal

def makeV2Shelf(rectangle, filename, params, numTabs=3):
    c = canvas.canvas()
    #make outer rectangle
    depth=math.fabs(rectangle.XDistance)
    height=params.canHeight + (2*(params.boardThickness+params.v2TabHorizontal))+ params.v2TabVertical
    outerRect=RotatableRectangle(
            YDistance=depth, 
            XDistance=height,
            origin=Point(-1*params.v2TabVertical,0)
            )
    c.stroke(rectanglePath(outerRect), cut)
    # Make Tabs
    for tab in shelfTabs(depth, height, params.boardThickness, numTabs, verticalOffset=-1*params.v2TabVertical):
        c.stroke(rectanglePath(tab), cut)
    if params.debug:
        c.stroke(path.path(path.moveto(0,0), path.lineto(0,40)), draw_debug)
        c.stroke(path.path(path.moveto(0,0), path.lineto(40,0)), draw_debug)
    c.writePDFfile("output/%s_v2"%filename)    

def makeShelf(rectangle, filename, params, numTabs=3):
    c = canvas.canvas()
    #make outer rectangle
    depth=math.fabs(rectangle.XDistance)
    height=params.canHeight + (2*params.boardThickness)
    outerRect=RotatableRectangle(
            YDistance=depth, 
            XDistance=height,
            origin=Point(0,0)
            )
    c.stroke(rectanglePath(outerRect), cut)
    # Make Tabs
    for tab in shelfTabs(depth, height, params.boardThickness, numTabs):
        c.stroke(rectanglePath(tab), cut)
    if params.debug:
        c.stroke(path.path(path.moveto(0,0), path.lineto(0,40)), draw_debug)
        c.stroke(path.path(path.moveto(0,0), path.lineto(40,0)), draw_debug)
    c.writePDFfile("output/%s_v1"%filename)    
    
def main():
    #create parameters object
    params = CanStackerParameters()
    
    #create the side wall
    sideWall = canvas.canvas()
    
    #outline
    rectangle=RotatableRectangle(XDistance=params.cabinetDepth, YDistance=params.cabinetHeight)
    shape = rectanglePath(rectangle)
    sideWall.stroke(shape, cut)
    
    #lower shelf
    sideWall.stroke(rectanglePath(params.lsRectangle), vector_engrave)
    strokeTabs(params.lsRectangle, sideWall, cut, numTabs=7)
    makeShelf(params.lsRectangle, "lowershelf", params, numTabs=7)

    #lower gate
    sideWall.stroke(rectanglePath(params.lgRectangle), vector_engrave)
    strokeTabs(params.lgRectangle, sideWall, cut, numTabs=2)
    makeShelf(params.lgRectangle, "lowergate", params, numTabs=2)
    makeV2Shelf(params.lgRectangle, "lowergate", params, numTabs=2)
    
    #top shelf
    sideWall.stroke(rectanglePath(params.tsRectangle), vector_engrave)
    strokeTabs(params.tsRectangle, sideWall, cut, numTabs=5)
    makeShelf(params.tsRectangle, "topshelf", params, numTabs=5)
    makeV2Shelf(params.tsRectangle, "topshelf", params, numTabs=5)
    
    #top gate
    sideWall.stroke(rectanglePath(params.tgRectangle), vector_engrave)
    strokeTabs(params.tgRectangle, sideWall, cut, numTabs=2)
    makeShelf(params.tgRectangle, "topgate", params, numTabs=2)

    #Back wall
    sideWall.stroke(rectanglePath(params.bwRectangle), vector_engrave)
    strokeTabs(params.bwRectangle, sideWall, cut, numTabs=5)
    makeShelf(params.bwRectangle, "backwall", params, numTabs=5)
    makeV2Shelf(params.bwRectangle, "backwall", params, numTabs=5)
    
    sideWall.writePDFfile("output/SideWall")    

if __name__ == "__main__":
    main()   
 

