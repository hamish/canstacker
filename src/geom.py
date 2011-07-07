from pyx import *
from math import *


def rect(startx, starty, oppx, oppy):
    return path.path(path.moveto(startx, starty), path.lineto(startx, oppy),
              path.moveto(startx, oppy), path.lineto(oppx, oppy),
              path.moveto(oppx, oppy), path.lineto(oppx, starty),
              path.moveto(oppx, starty), path.lineto(startx, starty))

