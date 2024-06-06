import numpy as np
import pygame as pyg
import sys

from math import hypot, tanh, sqrt
from Settings import *

class Point():
    def __init__(self, pos:tuple[float, float] = (0, 0), mass:float=1, radius:float=5):
        self.curPos:np.ndarray = np.array(pos, dtype=float)
        self.prev:np.ndarray = self.curPos
        self.velocity = np.zeros(2, dtype=float)
        self.radius = radius
        self.static = False
        self.mass = mass
        self.connectedSpring:list[Spring] = list()

    def get_curPos(self):
        return self.curPos.copy()

    def set_curPos(self, pos:tuple[float, float]):
        self.curPos = np.array(pos, dtype=float)

    def add_force(self, force:np.ndarray):
        self.force += force
    
    def set_force(self, force:np.ndarray):
        self.force = force
    
    def get_force(self):
        return self.force.copy()
    
    def set_static(self, state):
        self.static = state
    
    def get_velocity(self):
        return self.velocity.copy()

    def update(self, dt:float):
        if self.static: return

        netForce = np.zeros(2)
        
        for spring in self.connectedSpring:
            netForce += spring.get_force() * (1 if self == spring.get_origin_object() else -1)
        
        netForce += self.mass * GRAVITY * np.array((0, 1))

        if(self.curPos[1] < 0):
            self.curPos[1] = 0
            self.velocity[1] = abs(self.velocity[1]) * RESTITUTION

        if(self.curPos[1] > HEIGHT):
            self.curPos[1] = HEIGHT
            self.velocity[1] = -abs(self.velocity[1]) * RESTITUTION
            self.velocity[0] *= FRICTION
        
        if(self.curPos[0] > WIDTH):
            self.curPos[0] = WIDTH
            self.velocity[0] = -abs(self.velocity[0]) * RESTITUTION
        
        if(self.curPos[0] < 0):
            self.curPos[0] = 0
            self.velocity[0] = abs(self.velocity[0]) * RESTITUTION
    
        self.curPos += self.velocity*dt + 0.5*netForce/self.mass*dt*dt
        self.velocity += netForce/self.mass*dt
        velArray = self.velocity
        velArray = velArray*velArray
        if(velArray[0]+velArray[1] > MAX_VELOCITY**2): self.velocity *= MAX_VELOCITY/sqrt(velArray[0] + velArray[1])
        
    def add_spring(self, spring):
        self.connectedSpring.append(spring)

    def draw(self, screen):
        pyg.draw.circle(screen, (255, 0, 0), self.curPos, self.radius)

class Spring():
    def __init__(self, obj1:Point, obj2:Point, s:float, l:float, d:float) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.stiffness = s
        self.length = l
        self.damping = d
        self.force = np.zeros(2, dtype=float)
        self.curLength = l

        obj1.add_spring(self)
        obj2.add_spring(self)
        
    
    def update(self):
        vecLen = hypot(self.obj2.curPos[0]-self.obj1.curPos[0], self.obj2.curPos[1]-self.obj1.curPos[1])
        self.curLength = vecLen
        if vecLen < sys.float_info.epsilon:
            return
        normalVec = (self.obj2.get_curPos()-self.obj1.get_curPos())/vecLen
        
        force = (vecLen-self.length)*self.stiffness + normalVec.dot((self.obj2.get_velocity()-self.obj1.get_velocity()))*self.damping
        self.inTension = force > 0
        self.force = force*normalVec
    
    def get_force(self):
        return self.force
    
    def get_origin_object(self):
        return self.obj1
    
    def draw(self, screen):
        v = tanh((self.curLength-self.length)/self.length*2)
        color = (255*v, 0, 0) if v > 0 else (0, 255*v*-1, 0)
        pyg.draw.line(surface=screen, color=color, start_pos=self.obj1.curPos, end_pos=self.obj2.curPos, width=3)

class SpringMassBody():
    def __init__(self, points:list[Point]|None = None, springs:list[Spring]|None = None):
        self.points = points
        self.springs = springs

    def update(self):
        self.update_springs()
        
        for point in self.points:
            point.update(TIME_SKIP)
    
    def update_springs(self):
        if self.springs:
            for spring in self.springs:
                spring.update()

    def draw(self, screen):
        if self.springs:
            for spring in self.springs:
                spring.draw(screen)
        
        for point in self.points:
            point.draw(screen)
