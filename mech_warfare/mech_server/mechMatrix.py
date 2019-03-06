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

def getAngleBetween(vec1, vec2):
    """
    obtains the angle between 2 given vectors

    Math:
    -----
    let v1 be vec1
    let v2 be vec2

    v1.v2 = |v1| * |v2| * cos(theta)

                   v1.v2
    cos(theta) = ---------
                 |v1|*|v2|

                    v1.v2
    theta = acos( --------- )
                  |v1|*|v2|

    Parameters:
    -----------
    vec1 : vector <x,y,...> or vector <x,y,h> homogenious coordinates,  where h=0
        first vector to find angle bewteen
    vec2 : vector <x,y,...> or vector <x,y,h> homogenious coordinates,  where h=0
        second vector to find angle between
    """

    product_in_same_direction = np.inner(vec1, vec2) # numerator
    maximum_possible_product = np.linalg.norm(vec1) * np.linalg.norm(vec2) # denominator

    cos_theta = product_in_same_direction/maximum_possible_product

    return math.acos(cos_theta)


def _unoptimized_projectVectorOnto(vec_src, vec_dest):
    """
    most intunitive but computational less preferable method to show equivilance to real method

    projects the vec_src vector into the same direction as the vec_dest direction and gives back this projected vector

    this is simply the length along vec_dest such that it forms a 90 degree angle with vec_src end point

    Math:
    -----
    let v1 be source vector
    let v2 be destination vector

                          v2
    let v2-unit-vector = ----  (for destination direction)
                         |v2|

    let v1-magnitude-along-v2 = v1 * cos(theta)

    solution: v2-unit-vector * v1-magnitude-along-v2
    
               v2
    solution: ---- * |v1| * cos(theta)
              |v2|

    """
    theta = getAngleBetween(vec_src, vec_dest)

    dest_unit_vector = vec_dest/np.linalg.norm(vec_dest)

    projected_magnitude = np.linalg.norm(vec_src) * math.cos(theta)

    return dest_unit_vector * projected_magnitude



# define unoptimized and optimized versions of the code
def projectVectorOnto(vec_src, vec_dest):
    """
    projects the vec_src vector into the same direction as the vec_dest direction and gives back this projected vector

    this is simply the length along vec_dest such that it forms a 90 degree angle with vec_src end point

    Math:
    -----
    let v1 be source vector
    let v2 be destination vector

            v1.v2
    let A = -----
            v2.v2

    let B = v2

             v1.v2
    A * B =  ----- * v2 = v1
             v2.v2

    where A is a scalar
      and B is a vector

    A * B gives the vector direction given by B but with the magnitude for projected data from A * B = v1
    =============================================================
               v2
    solution: ---- * |v1| * cos(theta)    from function _unoptimized_projectVectorOnto
              |v2|

    
               v2                         |v2|
    solution: ---- * |v1| * cos(theta)  * ----
              |v2|                        |v2|

               v2              1
    solution: ---- * v1.v2  * ----
              |v2|            |v2|

              v1.v2
    solution: ----- * v2     (presuming |v2|*|v2| == v2.v2 for our use case)
              v2.v2

    Parameters:
    -----------
    vec_src : vector <x,y,h> homogenious coordinates (h=0) or non-homogenious coordinates
        vector that is being projected from. The vector being manipulated to match another direction
    vec_dest : vector <x,y,h> homogenious coordinates (h=0) or non-homogenious coordinates
        vector that is being projected into. The vector direction that is desired to be transformed into

    """

    src_dest_product = np.inner(vec_src, vec_dest) # A_numerator
    dest_squared = np.inner(vec_dest, vec_dest) # A_denominator

    src_magnitude_per_dest = src_dest_product/float(dest_squared) # A = A-numerator/A-denominator
    dest = vec_dest # B
    
    src_projected_onto_dest = src_magnitude_per_dest * dest # A * B

    return src_projected_onto_dest

