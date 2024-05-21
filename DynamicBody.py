import numpy as np

from Point import Point
from Settings import *
from Spring import Spring


class DynamicBody():
    def __init__(self, origin:tuple[float, float], points:list[Point]|None = None, springs:list[Spring]|None = None):
        self.points = points
        self.springs = springs

    def update(self):
        if self.springs:
            for spring in self.springs:
                spring.relax()
        
        for point in self.points:
            point.update(TIME_SKIP)
    
    def draw(self, screen):
        if self.springs:
            for spring in self.springs:
                spring.draw(screen)
        
        for point in self.points:
            point.draw(screen)