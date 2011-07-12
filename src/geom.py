from pyx import *
from math import *
from geom import *
from coordinates import *

def rect(startx, starty, oppx, oppy):
    return path.path(path.moveto(startx, starty), path.lineto(startx, oppy),
              path.moveto(startx, oppy), path.lineto(oppx, oppy),
              path.moveto(oppx, oppy), path.lineto(oppx, starty),
              path.moveto(oppx, starty), path.lineto(startx, starty))

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
                
