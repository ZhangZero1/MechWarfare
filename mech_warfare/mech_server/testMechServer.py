import pygame

import numpy as np
import math

import time
import signal
import sys
import errno

from legClassV3 import MechLeg
from bodyClassV3 import MechBody
#The new servo interface class.

import datetime

from MechServerConstants import *

bot = MechBody(np.matrix([100,100,1]),0.0,l_sweep,l_extend,square_offset,max_speed,rad_max,triangleExpand)

pygame.init()
screen = pygame.display.set_mode((500,500))

tLast = datetime.datetime.now()
tNow = datetime.datetime.now()

da_const = 15

def genResult(xDir, yDir):
    
    xCommand = (np.int8(xDir)/100.0)*max_speed 
    yCommand = (np.int8(yDir)/100.0)*max_speed

    return xCommand, yCommand

def genRot(rotation):
    return (np.int8(rotation)/100.0)*rad_max

def convCoord(xLoc, yLoc):
    MAX_X = 500
    MIN_X = 500

    CENTER_X = 250
    CENTER_Y = 250

    return CENTER_X + xLoc, CENTER_Y - yLoc

KEY_UP = False
KEY_DOWN = False
KEY_LEFT = False
KEY_RIGHT = False
KEY_CW = False # clockwise
KEY_CCW = False

while is_running:

    screen.fill((0,0,0))
    for item in bot.legList:
        item.renderLeg(bot.mech_to_world,screen)
    

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                is_running = False
            if event.key == pygame.K_w:
                KEY_UP = True
            if event.key == pygame.K_d:
                KEY_RIGHT = True
            if event.key == pygame.K_s:
                KEY_DOWN = True
            if event.key == pygame.K_a:
                KEY_LEFT = True
            if event.key == pygame.K_q:
                KEY_CCW = True
            if event.key == pygame.K_e:
                KEY_CW = True

            """
            elif event.key == pygame.K_w:
                x,y = genResult(0, -da_const)
                bot.setCommand(np.matrix([x,y,0]), 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                #bot.setCommand(np.matrix([0,-10,0]),0)
            elif event.key == pygame.K_a:
                x,y = genResult(-da_const, 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                #bot.setCommand(np.matrix([-10,0,0]),0)
            elif event.key == pygame.K_s:
                x,y = genResult(0, da_const)
                bot.setCommand(np.matrix([x,y,0]), 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                #bot.setCommand(np.matrix([0,10,0]),0)
            elif event.key == pygame.K_d:
                x,y = genResult(da_const, 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                bot.setCommand(np.matrix([x,y,0]), 0)
                #bot.setCommand(np.matrix([10,0,0]),0)
            """


            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                KEY_UP = False
            if event.key == pygame.K_d:
                KEY_RIGHT = False
            if event.key == pygame.K_s:
                KEY_DOWN = False
            if event.key == pygame.K_a:
                KEY_LEFT = False
            if event.key == pygame.K_q:
                KEY_CCW = False
            if event.key == pygame.K_e:
                KEY_CW = False
        """
        else:
            bot.setCommand(np.matrix([0,0,0]),0)
            bot.setCommand(np.matrix([0,0,0]),0)
        """

    """
    if len(events) == 0:
        bot.setCommand(np.matrix([0,0,0]),0)
        bot.setCommand(np.matrix([0,0,0]),0)
    """

    x = 0
    y = 0
    rot = 0
    if KEY_UP:
        x,y = genResult(0, -da_const)
    elif KEY_RIGHT:
        x,y = genResult(da_const, 0)
    elif KEY_LEFT:
        x,y = genResult(-da_const, 0)
    elif KEY_DOWN:
        x,y = genResult(0, da_const)
    
    if KEY_CW:
        rot = genRot(-da_const)
    elif KEY_CCW:
        rot = genRot(da_const)

    #print("x: %f. y: %f"%(x,y))


    bot.setCommand(np.matrix([x,y,0]), rot)
    bot.setCommand(np.matrix([x,y,0]), rot)

    #bot.setCommand(np.matrix([10,10,0]),0)
    #update
    tnow = datetime.datetime.now()
    #calculate how long it took (in seconds)
    t_elapsed = tnow-tLast
    period = t_elapsed.total_seconds() 
    #print period
    bot.updateState(period)
    tLast = datetime.datetime.now()

    #print(bot.legList[0].legTipPosition())
    #print(bot.legList[1].legTipPosition())
    #print(bot.legList[2].legTipPosition())
    #print(bot.legList[3].legTipPosition())

    """
    l1 = np.array([0,0,1])*bot.legList[0].leg_to_mech*bot.mech_to_world
    l2 = np.array([0,0,1])*bot.legList[1].leg_to_mech*bot.mech_to_world
    l3 = np.array([0,0,1])*bot.legList[2].leg_to_mech*bot.mech_to_world
    l4 = np.array([0,0,1])*bot.legList[3].leg_to_mech*bot.mech_to_world

    l1E = bot.legList[0].legTipPosition()*bot.mech_to_world
    l2E = bot.legList[1].legTipPosition()*bot.mech_to_world
    l3E = bot.legList[2].legTipPosition()*bot.mech_to_world
    l4E = bot.legList[3].legTipPosition()*bot.mech_to_world

    print(l1)
    print(l1E)

    for item in [[l1,l1E], [l2,l2E], [l3,l3E], [l4,l4E]]:
        item = np.array(item)
        xOld,yOld = convCoord(item[0][0][0], item[0][0][1])
        xNew,yNew = convCoord(item[1][0][0], item[1][0][1])

        pygame.draw.line(screen,
                        (255,0,0),
                        (xOld, yOld),
                        (xNew, yNew)
                        )
    """

    pygame.display.update()
    time.sleep(1.0/1000.0)
