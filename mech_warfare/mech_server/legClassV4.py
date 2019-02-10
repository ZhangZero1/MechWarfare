#! /usr/bin/python

#Jeremy Lim
#This class contains the info for a single leg of the mech.

#for rendering.
import pygame
#for matrix math.
import numpy as np
#general math
import math

#class MechLegMethod:

class MechLegVector:

    def __init__(self, vector):
        self.vector = vector

    def getVector():
        return self.vector
    
    

class MechLeg:

    def __init__(self,in_pixels_unit,in_max_range,in_angular_sweep,mech_leg_trans,mech_leg_rot,in_stand_pos,in_min_range=0):

        self.mech_to_leg = mech_leg_trans*mech_leg_rot 
        self.leg_to_mech = np.linalg.inv(mech_leg_rot)*np.linalg.inv(mech_leg_trans)

        self.pixels_per_u = in_pixels_unit

        #The Homogeneous position(in the leg's frame) the leg defaults to.
        self.stand_pos = in_stand_pos
        #The Homogeneous position(in the leg's frame) of our current leg position
        self.position = in_stand_pos
        #How far this idealized leg can extend
        self.max_range = in_max_range
        #How close to its base it can retract
        self.min_range = in_min_range
        self.angular_sweep = in_angular_sweep

        #center of rotation, relative to stand position
        self.pivot_pos = np.matrix([0,0,0])
        #speed in radians, around the pivot position
        #+ or -
        self.radSpeed = 0.0

        #l1 homogenous end coord: one edge which the leg vector can turn between
        self.l1Pt = np.matrix([self.max_range*math.cos((math.pi-self.angular_sweep)/2.0),self.max_range*math.sin((math.pi-self.angular_sweep)/2.0),1.0])
        #l2 homogenous end coord: other edge which the leg vector can turn between
        self.l2Pt = np.matrix([-self.max_range*math.cos((math.pi-self.angular_sweep)/2.0),self.max_range*math.sin((math.pi-self.angular_sweep)/2.0),1.0])

        #Target position, in self coords.
        #Homogeneous
        self.target = self.stand_pos
        #Last given speed command. How fast we move to our target.
        #units per second.
        self.speed = 0
        self.grounded = True  #are we on the ground, or not
 
    def setTarget(self,in_position,in_speed):
        """
        issues a new target for the leg to attempt to reach at a given speed

        Parameters
        ----------
        in_position: vector<x,y,h> homogenious coordinates
            a vector for the new position to reach
            leg coordinate space
        in_speed: float
            represents how fast the leg needs to reach this point
        """
        self.speed = in_speed
        self.target = in_position
        self.radSpeed = 0.0

    
    def setTargetExtend(self,in_direction,in_speed):
        """
        Sets a new target and speed to reach the target by specifying how far
        to move in what direction to reach the target

        Parmaters:
        ----------
        in_direction: vector <x,y,h> homogenious coordinates
            a vector of how far to move the current location to reach the target
            given in mech coordinate space
        in_speeed: float
            represents how fast the leg needs to move to reach this point

        """
        self.speed = in_speed
        self.target = self.position+(in_direction*self.mech_to_leg)
        self.radSpeed = 0.0

    def setTargetAngleExtend(self,in_angle,in_radspeed,in_pivot):
        """
        Sets a new target to reach via rotating the current location of the leg
        around some given pivot point

        Parmaters:
        ----------
        in_angle: Angle
            an angle for how much to rotate around the pivot for
        in_radspeed: float
            gives how fast the rotation must occur
        in_pivot: vector<x,y,h> homogenious coordinates
            gives the position of the pivot to rotate along
            (leg coordinate space???)
        """

        #COMPLETED: offload direction data to rad_speed variable
        pass




    



