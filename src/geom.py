from pyx import *
from math import *
from geom import *
from coordinates import *
import trig

def rect(startx, starty, oppx, oppy):
    return path.path(path.moveto(startx, starty), path.lineto(startx, oppy),
              path.moveto(startx, oppy), path.lineto(oppx, oppy),
              path.moveto(oppx, oppy), path.lineto(oppx, starty),
              path.moveto(oppx, starty), path.lineto(startx, starty))

def shelfTabs(depth, height, tabThickness, numTabs=3, verticalOffset=0):
    numPositions=(2*numTabs)-1
    tabLength=depth/numPositions
    result=[]
    for i in range(numTabs-1):
    	o1 = Point(0,((2*i+1)*tabLength)+verticalOffset)
    	print "****************tab %d, origin="%i , o1
        rect=RotatableRectangle(
            origin=o1,
            XDistance=tabThickness,
            YDistance=tabLength)
        result.append(rect)
        rect=RotatableRectangle(
            origin=Point(height,(2*i+1)*tabLength),
            XDistance=-1*tabThickness,
            YDistance=tabLength)
        result.append(rect)
    return result
        
def tabCuts(rectangle, numTabs=3):
    numPositions=(2*numTabs)-1
    # at present cut in the rectangles original x dimension
    tabLength = rectangle.XDistance/numPositions
    result=[]
    print "tabLength=", tabLength
    print "rectangle.XDistance=", rectangle.XDistance
    print "rectangle.angle=", rectangle.angle
    print
    for i in range(numTabs):
        hyp = 2*tabLength*i
        adj=trig.getAdjacent(hypotenuse=hyp, angle=rectangle.angle)
        opp=trig.getOpposite(hypotenuse=hyp, angle=rectangle.angle)
        originX=rectangle.origin.x+ adj
        originY=rectangle.origin.y+ opp
        origin=Point(originX, originY)
        print "*** TAB ", i
        print "hyp=", hyp
        print "adj/opp", adj, "/", opp
        print "origin=", origin
        rect=RotatableRectangle(origin=origin,
                            XDistance=tabLength, 
                            YDistance=rectangle.YDistance, 
                            angle=rectangle.angle
                            )
        result.append(rect)
    return result
    
def rectanglePath(rectangle):
    a=rectangle.getPosA(); #print a
    b=rectangle.getPosB(); #print b
    c=rectangle.getPosC(); #print c
    d=rectangle.getPosD(); #print d
    return path.path(
        path.moveto(a.x,a.y), path.lineto(b.x,b.y),
        path.moveto(b.x,b.y), path.lineto(c.x,c.y),
        path.moveto(c.x,c.y), path.lineto(d.x,d.y),
        path.moveto(d.x,d.y), path.lineto(a.x,a.y)
    )


class RotatableRectangle:
    """A rectangle on a cartesian plane. point of origin, height, width and
    angle can be set. It is ok to set any of the parameters to negative values.
    Angle is specified in degrees.
    
    """
    def __init__(self, XDistance, YDistance, origin=Point(0.0,0.0), angle=0.0):
        self.origin=origin
        self.XDistance=float(XDistance)
        self.YDistance=float(YDistance)
        self.angle=float(angle)

        
    def getPosA(self):
        return self.origin.clone()
    def getPosB(self):
        intermediate=self.getPosA().clone()
        intermediate.slide_xy(self.XDistance, 0.0)
        posB=intermediate.rotate_about(self.origin.clone(), self.angle)
        return posB
    def getPosC(self):
        intermediate = self.getPosA().clone()
        intermediate.slide_xy(self.XDistance, self.YDistance)    
        posC=intermediate.rotate_about(self.origin.clone(), self.angle)
        return posC
    def getPosD(self):
        intermediate=self.getPosA().clone()
        intermediate.slide_xy(0.0,self.YDistance)
        posD=intermediate.rotate_about(self.origin.clone(), self.angle)
        return posD
            
    def getVertices(self):
        return (self.getPosA(),
                self.getPosB(),
                self.getPosC(),
                self.getPosD()
                )
                
