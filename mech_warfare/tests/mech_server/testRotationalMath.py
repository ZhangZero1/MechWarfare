from mech_warfare.mech_server import RotationalMath

import unittest
import numpy as np

import math

class Test_Radius(unittest.TestCase):

    def __init__(self, *args, **argw):
        super(Test_Radius, self).__init__(*args, **argw)


    def test_getVector(self):

        verify = lambda arr1, arr2: self.assertTrue(  np.array_equal(arr1, arr2)  )
        
        pos1 = np.array([10, 10, 1])
        pos2 = np.array([7, 2, 1]) # must be a position, h=1

        piv = np.array([5, 5, 1])

        r1 = RotationalMath.Radius(piv, pos1)
        r2 = RotationalMath.Radius(piv, pos2)

        verify( r1.getVector(), np.array([5, 5, 0])  )  # gives back a relative distance, h=0
        verify( r2.getVector(), np.array([2, -3, 0])  )


    def test_getValue(self):
        verify = lambda val1, val2: self.assertTrue(  
                   np.allclose(
                       np.array([val1]), 
                       np.array([val2])
                    )  
                )
        
        pos1 = np.array([10, 10, 1])
        pos2 = np.array([7, 2, 1]) # must be a position, h=1

        piv = np.array([5, 5, 1])

        r1 = RotationalMath.Radius(piv, pos1)
        r2 = RotationalMath.Radius(piv, pos2)


        verify( r1.getValue(), 5 * math.sqrt(2)  )  # gives back a relative distance, h=0
        verify( r2.getValue(), math.sqrt(2**2 + 3**2)  )

    def test_equality(self):
        r1 = RotationalMath.Radius( np.array([5,5,1]), np.array([3,3,1]) )
        r2 = RotationalMath.Radius( np.array([5,5,1]), np.array([3,3,1]) )
        r3 = RotationalMath.Radius( np.array([3,5,1]), np.array([3,2,1]) )

        self.assertNotEqual(r1, r3)
        self.assertNotEqual(r3, r2)
        self.assertEqual(r1, r2)
        self.assertEqual(r2, r1)



class Test_RotationalMeasurement(unittest.TestCase):

    def __init__(self, *args, **argw):
        super(Test_RotationalMeasurement, self).__init__(*args, **argw)

    def test_equality(self):
        pivot = np.array([5,5,1])
        pos1 = np.array([3, 3, 1])
        r1 = RotationalMath.Radius( pivot, pos1)
        r2 = RotationalMath.Radius( pivot, pos1)

        rotMeasure1 = RotationalMath.RotationalMeasurement(10, True, r1)
        rotMeasure2 = RotationalMath.RotationalMeasurement(10, True, r2)

        self.assertEqual(rotMeasure1, rotMeasure2)
        self.assertEqual(rotMeasure2, rotMeasure1)

    def test_convertTo_same(self):
        pivot = np.array([5,5,1])
        pos1 = np.array([3, 3, 1])
        r1 = RotationalMath.Radius( pivot, pos1)
        r2 = RotationalMath.Radius( pivot, pos1)

        rotMeasure1 = RotationalMath.RotationalMeasurement(10, True, r1)
        rotMeasure2 = RotationalMath.RotationalMeasurement(10, True, r2)

        self.assertEqual(rotMeasure1.convertTo(True), rotMeasure2)

    def test_convertTo(self):
        pivot = np.array([5,5,1])
        pos1 = np.array([5, 7, 1])

        r1 = RotationalMath.Radius( pivot, pos1)

        rotMeasure1 = RotationalMath.RotationalMeasurement(10, True, r1)
        rotMeasure2 = RotationalMath.RotationalMeasurement(20, False, r1) 

        self.assertEqual(rotMeasure1.convertTo(False), rotMeasure2)

        

        






        



def __perform_test__():
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_Radius)
    unittest.TextTestRunner(verbosity=2).run(suite)

    suite = unittest.TestLoader().loadTestsFromTestCase(Test_RotationalMeasurement)
    unittest.TextTestRunner(verbosity=2).run(suite)
