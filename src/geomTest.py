import unittest
from geom import *
from coordinates import *

class SimpleTest(unittest.TestCase):
    def testNoRotate(self):
        rectangle=RotatableRectangle(XDistance=1, YDistance=2)
        self.assertEqual(rectangle.getPosA(), Point(0.0,0.0))
        self.assertEqual(rectangle.getPosB(), Point(1.0,0.0))
        self.assertEqual(rectangle.getPosC(), Point(1.0,2.0))
        self.assertEqual(rectangle.getPosD(), Point(0.0,2.0))

    def testRotate90(self):
        rectangle=RotatableRectangle(XDistance=1, YDistance=2, angle=90)
        self.assertEqual(rectangle.getPosA(), Point(0.0,0.0))
        self.assertEqual(rectangle.getPosB(), Point(0.0,1.0))
        self.assertEqual(rectangle.getPosC(), Point(-2.0,1.0))
        self.assertEqual(rectangle.getPosD(), Point(-2.0,0.0))

    def testRotate45(self):
        a=math.sin(math.radians(45))*10
        rectangle=RotatableRectangle(XDistance=10, YDistance=10, angle=45)
        #print rectangle.getVertices()
        self.assertEqual(rectangle.getPosA(), Point(0.0,0.0))
        self.assertEqual(rectangle.getPosB(), Point(a,a))
        self.assertEqual(rectangle.getPosC(), Point(0.0,2*a))
        self.assertEqual(rectangle.getPosD(), Point(-1*a,a))
if __name__ == "__main__":
    unittest.main()   
    
    
    


