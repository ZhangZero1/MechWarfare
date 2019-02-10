class LinearEquation(object):

    def __init__(self, mode):
        self.mode = mode

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
