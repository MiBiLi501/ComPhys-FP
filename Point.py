import numpy as np
import pygame as pyg

from Settings import *

class Point():
    def __init__(self, pos:tuple[float, float] = (0, 0), mass:float=1):
        self.curPos:np.ndarray = np.array(pos, dtype=float)
        self.prev:np.ndarray = self.curPos
        self.velocity = np.zeros(2, dtype=float)
        self.force = np.array((0, GRAVITY), dtype=float)
        self.radius = 10
        self.static = False
        self.mass = mass

    def add_force(self, force:np.ndarray):
        self.force += force
    
    def set_force(self, force:np.ndarray):
        self.force = force

    def update(self, dt:float):
        # temp_velocity = 2*self.curPos - self.prev + self.force/self.mass*dt*dt
        # self.prev = self.curPos
        # self.curPos = temp_velocity
        self.curPos += self.velocity*dt + 0.5*self.force/self.mass*dt*dt
        self.velocity += self.force/self.mass*dt
        
    
    def draw(self, screen):
        pyg.draw.circle(screen, (255, 0, 0), self.curPos, self.radius)