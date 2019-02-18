from mech_warfare.mech_server import mechMatrix
import numpy as np
import math

import unittest

class Test_MechMatrix(unittest.TestCase):
    def __init__(self, *args, **argv):
        #implement super here
        super(Test_MechMatrix, self).__init__(*args, **argv)

        self.horizontalVector = np.array([5,0,1])
        self.verticalVector = np.array([0,5,1])

    def test_makeTranslationMatrix(self):
        xShift = 3
        yShift = 2

        expectedVector = self.horizontalVector + np.array([xShift, yShift, 0])
        actualVector = self.horizontalVector * mechMatrix.makeTranslationMatrix(xTrans=xShift, yTrans=yShift)
        actualVector = np.array(actualVector)[0]

        self.assertTrue(np.array_equal(expectedVector, actualVector))

    def test_makeRotationMatrix(self):
        rotation = math.pi/2.0

        expectedVector = self.horizontalVector

        actualVector = self.verticalVector * mechMatrix.makeRotationMatrix(rotate=rotation, isClockwise=False)
        actualVector = np.array(actualVector)[0]

        self.assertTrue(np.allclose(expectedVector, actualVector))

        expectedVector = self.verticalVector

        actualVector = self.horizontalVector * mechMatrix.makeRotationMatrix(rotate=rotation, isClockwise=True)
        actualVector = np.array(actualVector)[0]

        self.assertTrue(np.allclose(expectedVector, actualVector))

    def test_transformVector(self):
        translation = mechMatrix.makeTranslationMatrix(xTrans=0, yTrans=3)
        rotation = mechMatrix.makeRotationMatrix(rotate=math.pi/2.0, isClockwise=False)

        actualVector = mechMatrix.transformVector(self.verticalVector,
                                                  [translation, rotation])

        expectedVector = np.array([8, 0, 1])

        self.assertTrue(np.allclose(expectedVector, actualVector))






def __perform_test__():
        """
	x = np.array([0,0,1])
	y = mechMatrix.makeTranslationMatrix(xTrans=5,yTrans=5)
	 

	res = x*y

	print("we start from:")
	print(x)
	print("using translation matrix:")
	print(y)
	print("we end up at")
	print(res)


        x = np.array([5,5,1])
        d = mechMatrix.makeRotationMatrix(rotate=math.pi/2)
        
        res = x*d
        
	print("we start from:")
	print(x)
	print("using translation matrix:")
	print(d)
	print("we end up at")
	print(res)

        """

        suite = unittest.TestLoader().loadTestsFromTestCase(Test_MechMatrix)
        unittest.TextTestRunner(verbosity=2).run(suite)
