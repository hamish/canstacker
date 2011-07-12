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
        self.canHeight=float(110)
        self.canDiameter=float(80)
        
        self.minFingerDistance=float(30)
        self.minShelfAngle=float(2)
        
        self.margin=float(7)
        self.frontGap=float(1)
        self.backGap=float(10)
    
    
        #Calculated Parameters
        self.lowerGateHeight=self.canDiameter/4
        self.UpperGateHeight=self.canDiameter/8
        self.cabinetHeight = float(400) # TODO - calculate this value
        
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
        
        
        lgOrigin=self.lsRectangle.getPosD().clone()
        lgOrigin.slide_xy(0,self.frontGap)
        ##### Front Gate
        self.lgRectangle=RotatableRectangle(
            XDistance=-1*self.boardThickness, 
            YDistance=self.lowerGateHeight,
            origin=lgOrigin
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
        
        
        self.lsTranslationDistanceX = cos(90-self.minShelfAngle)*self.boardThickness
        self.lsTranslationDistanceY = sin(90-self.minShelfAngle)*self.boardThickness
        self.lsTopFrontX=self.lsBottomFrontX+self.lsTranslationDistanceX
        self.lsTopFrontY=self.lsBottomFrontY+self.lsTranslationDistanceY
        self.lsTopBackX=self.lsBottomBackX+self.lsTranslationDistanceX
        self.lsTopBackY=self.lsBottomBackY+self.lsTranslationDistanceY
        
        # Top Shelf
        self.tsBottomBackX=self.margin+self.boardThickness+self.canDiameter+self.backGap
        self.tsBottomBackY=self.lsTopBackY+self.canDiameter
        self.tsBottomFrontX=self.cabinetDepth
        self.tsBottomXDistance = self.tsBottomFrontX-self.tsBottomBackX
        self.tsBottomFrontY= tan(self.minShelfAngle)*self.tsBottomXDistance
        
        #tan angle = Opposite/Adjacent



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

    #lower gate
    sideWall.stroke(rectanglePath(params.lgRectangle), vector_engrave)

    #top shelf
    sideWall.stroke(rectanglePath(params.tsRectangle), vector_engrave)


    sideWall.writeEPSfile("output/SideWall")    

if __name__ == "__main__":
    main()   
 

