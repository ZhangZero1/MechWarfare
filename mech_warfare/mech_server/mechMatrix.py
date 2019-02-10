import math
import numpy as np

def makeTranslationMatrix(xTrans, yTrans):

    """
    Produces a translation matrix that can move an applied vector(head) by some x and y 
    direction.

    Parameters:
    -----------
    xTrans: float
        how much to shift the x position
    yTrans: float
        how much to shift the y position
    """
    return np.transpose(
        np.matrix(
            [
                [1,0, xTrans],
                [0,1, yTrans],
                [0,1, 1]
            ]
        )
    )

def makeRotationMatrix(rotate):

    """
    produces a rotation matrix that can rotate(from tail, <0,0>) an applied vector CW by the
    given amount in radians

    Parameters
    ----------
    rotate : float
        the radians for how much the rotation matrix should rotate by


    """
    
    cose = math.cos(rotate)
    sine = math.sin(rotate)

    return np.matrix(
        [
            [cose, -sine, 0],
            [sine,  cose, 0],
            [   0,     0, 1],
        ]
    )






