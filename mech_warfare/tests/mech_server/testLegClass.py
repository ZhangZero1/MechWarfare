import unittest

from mech_warfare.mech_server import legClassV4
from mech_warfare.mech_server import mechMatrix

import math

import numpy as np

import pygame

import copy


class Test_LegClass(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Test_LegClass, self).__init__(*args, **kwargs)

        self.leg1 = legClassV4.MechLeg(
                        in_pixels_unit=1,
                        in_max_range=12,
                        in_angular_sweep=math.pi/2.0,
                        mech_leg_trans=mechMatrix.makeTranslationMatrix(-5,-5),
                        mech_leg_rot=mechMatrix.makeRotationMatrix(-math.pi/4.0),
                        in_stand_pos=np.array([0,0,1]),
                        in_min_range=0
                )

    def test_setTarget(self):
        test_leg = copy.deepcopy(self.leg1)

        test_leg.setTarget( np.array([0,0,1]), 12) 

        self.assertEqual(test_leg.speed, 12)
        self.assertTrue(np.array_equal(test_leg.target, np.array([0,0,1])))
        self.assertEqual(test_leg.radSpeed, 0.0)

    def test_setTargetExtend(self):
        test_leg = copy.deepcopy(self.leg1)

        test_leg.setTargetExtend(np.array([1, 1, 0]),12 ) # note the use of h=0 for extension, this means direction not distance

        expectedLeg = np.array([0, math.sqrt(2), 1])

        self.assertTrue(np.allclose(test_leg.target, expectedLeg))

    def test_setTargetAngleExtend(self):
        test_leg = copy.deepcopy(self.leg1)

        pivot = np.array([4, 4, 1])

        test_leg.setTargetAngleExtend(math.pi, 3, pivot)
        expectedLeg = np.array([0, -2*math.sqrt(2), 1])

        self.assertTrue(np.allclose(test_leg.target, expectedLeg))

        test_leg = copy.deepcopy(self.leg1)

        test_leg.setTargetAngleExtend(math.pi/2.0, 3, pivot)
        expectedLeg = np.array([-math.sqrt(2), -math.sqrt(2), 1])

        self.assertTrue(np.allclose(test_leg.target, expectedLeg))

    def test_specialProjectExtend(self):
        test_leg = copy.deepcopy(self.leg1)
        test_leg.position = np.array([5, 5, 1])

        new_dir = np.array([3, 0,0])

        test_leg.specialProjectExtend(new_dir, 0, 2)

        expectedLeg = np.array([7, 0, 1])
        actualLeg = test_leg.target
        
        self.assertTrue(np.allclose(expectedLeg, actualLeg))




        


def __perform_test__():
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_LegClass)
    unittest.TextTestRunner(verbosity=2).run(suite)

