from math import sqrt, hypot
import numpy as np
import pygame as pyg

from Point import Point

class Spring():
    def __init__(self, obj1:Point, obj2:Point, s:float, l:float, d:float) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.stiffness = s
        self.length = l
        self.damping = d
        self.prev = np.zeros(2, dtype=float)
    
    def relax(self):
        self.obj1.add_force(-self.prev)
        self.obj2.add_force(self.prev)
        vecLen = hypot(self.obj2.curPos[0]-self.obj1.curPos[0], self.obj2.curPos[1]-self.obj1.curPos[1])
        if vecLen < 0.000000000001:
            return
        normalVec = (self.obj2.curPos-self.obj1.curPos)/vecLen
        
        force = (vecLen-self.length)*self.stiffness + normalVec.dot((self.obj2.velocity-self.obj1.velocity))*self.damping
        # print(type(force))
        self.obj1.add_force(force*normalVec)
        self.obj2.add_force(force*-normalVec)
        self.prev = force*normalVec
    
    def draw(self, screen):
        pyg.draw.line(surface=screen, color=(0, 0, 255), start_pos=self.obj1.curPos, end_pos=self.obj2.curPos)