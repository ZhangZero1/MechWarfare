class GeneralEquation(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def solve(self, x, y):
        return a*x + b*y + c

class SlopeInterceptEquation(object):
    def __init__(self, slope, intercept):
        super(SlopeInterceptEquation, self).__init__()

        self.slope = slope
        self.intercept = intercept


class Term(object):
    def __init__(self, coefficent, value=None):
        super(Term, self).__init__()

        self.coefficent = coefficent
        self.value = value

    def solve(self, value=None):
        if(value is None):
            return self.coefficent*value

        return sefl.coefficent * self.value

    def multiplyBy(self, value):
        new_coefficent = self.coefficent * value

        return Term(new_coefficent, self.value)

    def getCoefficent(self):
        return self.coefficent

class LinearEquation(object):
    def __init__(self, a, b, c):
        super(LinearEquation, self).__init__()

        self.LHS = Term(a, "x") + Term(b, "y") + c
        self.RHS = 0


    def rearrangeForY(self):
        RHS = self.RHS

        RHS = 




     


class LinearEquationConverter(object):
    def __init__(self):
        super(LinearEquationConverter, self).__init__()

    def toSlopeIntercept(self, genEquation):
        """

        Math:
        -----

        a*x + b*y + c = 0

        a*x + b*y = -c

        b*y = -c -(a*x)

                c       a
        y = - (---) - (---) * x
                b       b
                       a
        slope(m) = - (---)
                       b

                           c
        intercept(b) = - (---)
                           b
        """
        slope = -genEquation.getA() / float(genEquation.getB())
        intercept = -genEquationgetC()/ float(genEquation.getB())

        return SlopeInterceptEquation(slope, intercept)

    def toGeneral(self, slope, intercept):
        """

                       a
        slope(m) = - (---)
                       b

                           c
        intercept(b) = - (---)
                           b

        assume b = 1

        a = -1 * slope
        a = - slope

        c = -1 * intercept
        c = - intercept
        """

        a = -slope
        b = 1
        c = -intecept




class LinearEquation(object):
    def __init__(self, x1, y1, x2, y2):
        deltaX = x2 - x1
        deltaY = y2 - y1

        self.slope = deltaY/float(deltaX)

    def _convToSlopeIntercept(self, a, b, c):
        relation = 
        
        ["(-c/b)"] + ["(-a/b)", "*", "x"]

        firstTerm = 0
        secondTerm = 1
        coefficent = 0

        slope_sec = relation[firstTerm]
        intercept_sec = relation[secondTerm][coefficent]




        

"""
class LinearEquationBase(object):

    # create function generateSlope(a,b)... creates a slope object
    # or create function makeLinearEquation(x1, x2, y1, y2)

    def __init__(self):

        self.a = None
        self.b = None
        self.c = None

    def isInit(self):
        return self.a is not None and self.b is not None and self.c is not None

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def getSlope(self):
        return -self.a/self.b

    def getIntercept(self):
        return -self.c/self.b

    def setSlopeIntercept(self, slope, intercept):
        self.setSlope(slope)
        self.setIntercept(intercept)

    def setSlope(self, slope):
        self.a = -slope * self.b

    def setIntercept(self, intercept):
        self.c = -intercept * self.b

    def solve(self, x, y):
        return self.a*x + self.b*y + self.c

class LinearEquation(object):
    def __init__(self):
        super(LinearEquation, self).__init__()
"""
