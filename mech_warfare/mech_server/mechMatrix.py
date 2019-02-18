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
                [0,0, 1]
            ]
        )
    )

def makeRotationMatrix(rotate, isClockwise=False): # verify h=0 vs h=1 case

    """
    produces a rotation matrix that can rotate(from tail, <0,0>) an applied vector by the
    given amount in radians in the given direction

    Parameters
    ----------
    rotate : float
        the radians for how much the rotation matrix should rotate by
    isClockwise: boolean (default: True)
        is the rotation matrix turning clockwise


    """
    
    cose = math.cos(rotate)
    sine = math.sin(rotate)

    counter_clockwise_mat = np.matrix(
        [
            [cose, -sine, 0],
            [sine,  cose, 0],
            [   0,     0, 1],
        ]
    )

    if(isClockwise):
        return np.transpose(counter_clockwise_mat)
    else:
        return counter_clockwise_mat

def transformVector(vec, matrixList):
    
    """
    transforms the given vector by the given sequence of transformation matricies

    Parameters
    ----------
    vec : Vector <x,y,h> homogenious coordinates
        the input vector to transform 
    matrixList : List <Matrix{3x3} homogenious transformation matrix>
        the list of 3x3 transformation matricies to perform on sequence on the given vector
    """

    if(len(matrixList) == 0):
        return vec
    resultMatrix = vec*matrixList[0]
    resultVector = np.array(resultMatrix)[0]

    return transformVector(resultVector, matrixList[1:])


