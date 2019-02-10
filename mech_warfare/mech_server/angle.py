import math

class Angle(object):
    
    def __init__(self, angle, mode):
        self.angle = angle
        self.mode = mode


        self.period = {
            "radians" : 2*math.pi,
            "degrees" : 360
        }
        self.conversionRate = {
            "radians" : self.period("radians")/self.period("degrees"),
            "degrees" : self.period("degrees")/self.period("radians")
        }

    def setMode(self, mode):
        if(self.mode != mode):
            self.angle = self.angle * self.conversionRate[self.angle]
            self.mode = mode

    def setAngle(self, angle):
        self.angle = angle

    def getAngle(self):
        return self.angle

    def getMode(self):
        return self.mode

    def getPeriod(self):
        return self.period[self.mode]

def convertPeriod(angle, periodCount):
    currPeriodCount = int(angle.getAngle/angle.getPeriod)
    periodDifference = periodCount - currPeriodCount
    angleDifference = periodDifference * angle.getPeriod

    return Angle(angle.getAngle() + angleDifference, angle.getMode())


