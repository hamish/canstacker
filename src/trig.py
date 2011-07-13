import unittest
from math import *

def getHypotenuse(opposite=None, adjacent=None, angle=None):
    if opposite is None and (adjacent is not None and angle is not None):
        return adjacent/cos(radians(angle))
    raise Exception('unimplemented')


def getAdjacent(opposite=None, hypotenuse=None, angle=None):
    if opposite is None and (hypotenuse is not None and angle is not None):
        if hypotenuse==0:
            return 0.0
        return cos(radians(angle))*hypotenuse
    raise Exception('unimplemented')

def getOpposite(hypotenuse=None, adjacent=None, angle=None):
    if adjacent is None and (hypotenuse is not None and angle is not None):
        if hypotenuse==0:
            return 0
        return sin(radians(angle))*hypotenuse
    raise Exception('unimplemented')

class TrigTests(unittest.TestCase):
    def testGetHypotenuse(self):
        self.assertEqual(getHypotenuse(adjacent=1, angle=0), 1.0)        

    def testAdjacent(self):
        self.assertEqual(getAdjacent(hypotenuse=1, angle=0), 1.0)

    def testOpposite(self):
        self.assertEqual(getOpposite(hypotenuse=1, angle=0), 0.0)

    def testImpossibleCases(self):
        with self.assertRaises(Exception):
            # angle=0 and opposite!=0 is not possible
            getHypotenuse(opposite=1, angle=0)
            # hypotenuse for angle=0 and opposite!=0 is undefined            
            getHypotenuse(opposite=0, angle=0)

if __name__ == "__main__":
    unittest.main()   
    
