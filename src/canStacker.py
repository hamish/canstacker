from pyx import *
from math import *
from geom import *

unit.set(defaultunit="mm")

debug=0
engrave_outline=1

# Master Parameters. All units in mm
boardThickness=float(3)
cabinetDepth=float(390)

# these have some extra room built in so we can create a  
# space exactly canHeight or canDiameter and assume that 
# a real can will fit.
canHeight=float(110)
canDiameter=float(80)

minFingerDistance=float(30)
minShelfAngle=float(2)

margin=float(7)
frontGap=float(1)
backGap=float(10)

#Calculated Parameters
lowerGateHeight=canDiameter/4
UpperGateHeight=canDiameter/8
cabinetHeight=???

# lower shelf. Calculate based on minFingerDistance, then compare to minShelfAngle
lsBottomFrontX=cabinetDepth-gap
lsBottomFrontY=margin

lsBottomBackX=margin+boardThickness+gap
lsBottomXDistance = lsBottomFrontX-lsBottomBackX
lsBottomBackY=tan(minShelfAngle)*lsBottomXDistance

lsTranslationDistanceX = cos(90-minShelfAngle)*boardThickness
lsTranslationDistanceY = sin(90-minShelfAngle)*boardThickness
lsTopFrontX=lsBottomFrontX+lsTranslationDistanceX
lsTopFrontYlsBottomFrontY+lsTranslationDistanceY
lsTopBackX=lsBottomBackX+lsTranslationDistanceX
lsTopBackY=lsBottomBackYlsTranslationDistanceY

# Top Shelf
tsBottomBackX=margin+boardThickness+canDiameter+gap
tsBottomBackY=lsTopBackY+canDiameter
tsBottomFrontX=cabinetDepth
tsBottomXDistance = tsBottomFrontX-tsBottomBackX
tsBottomFrontY= tan(minShelfAngle)*tsBottomXDistance

#tan angle = Opposite/Adjacent

def sideWall(originX=0, originY=0):
    # Engrave the outer perimeter
    left=originX
    lower=originY
    right=left+cabinetDepth
    upper=lower+margin+