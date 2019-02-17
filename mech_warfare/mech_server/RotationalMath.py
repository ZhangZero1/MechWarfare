import math
import numpy as np

class Radius(object):

    def __init__(self, pivot, end_position):
        super(Radius, self).__init__()

        self.pivot = pivot
        self.end_position = end_position

        self.radius = self.end_position - self.pivot

    def getVector(self):
        return self.radius

    def getValue(self):
        return np.linalg.norm(self.radius)

    def _getPivot(self):
        return self.pivot

    def _getEndPos(self):
        return self.end_position

    def __eq__(self, radius_2):
        verification_test = [  np.array_equal(self.pivot , radius_2._getPivot() ),
                               np.array_equal(self.end_position , radius_2._getEndPos() ),
                               np.array_equal(self.radius , radius_2.getVector() )
                            ]
        
        all_true = lambda a, b : a and b

        return reduce(all_true, verification_test)

class RotationalMeasurement(object):

    def __init__(self, value, isRotational, radius):
        """
        
        Parameters
        ----------
        value : Numeric
            the current value of measurement given in the rotational mode (rotational or translational) mechanics
        isRotational: Boolean
            the mode of the given value is Rotational mechanic measurement or translational mechanics measurement
        radius: Radius
            the object representing the radius which the measurement measures traversal along circular motion
        """
        super(RotationalMeasurement, self).__init__()

        self.isRotational = isRotational
        self.value = value
        self.radius = radius

    def getValue(self):

        return self.value

    def getIsRotation(self):

        return self.isRotational

    def getRadius(self):
        return self.radius

    def convertTo(self, toRotational):
        """
        Makes a new version of the rotational measurement object with the specified isRotational mode and the converted
        value of the RotationalMeasurement object for that mode

        Parameters:
        -----------
        toRotational : boolean
            should convert to isRotational=True mode. Otherwise convert to isRotational=False mode.
            In short, for the converted object what should the isRotational mode be?

        """
        if(toRotational == self.isRotational):
            return RotationalMeasurement(self.value, self.isRotational, self.radius)
        
        new_value = None

        if(toRotational is True):
            new_value = self.value / self.radius.getValue()
        else:
            new_value = self.value * self.radius.getValue()

        return RotationalMeasurement(new_value, toRotational, self.radius)

    def __eq__(self, rot_measure_2):
        verification = [
                            self.isRotational == rot_measure_2.getIsRotation(),
                            self.radius == rot_measure_2.getRadius(),
                            self.value == rot_measure_2.getValue()
                        ]

        all_true = lambda a, b: a and b

        return reduce(all_true, verification)



