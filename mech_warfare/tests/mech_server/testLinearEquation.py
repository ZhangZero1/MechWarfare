import unittest
import numpy as np
import math

from mech_warfare.mech_server import linearEquation

class Test_LinearEquation(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test_LinearEquation, self).__init__(*args, **kwargs)

    def test_isInit(self):
        eq = linearEquation.LinearEquation()

        

        
