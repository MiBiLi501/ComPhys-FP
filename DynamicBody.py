from Point import Point
from Spring import Spring


class DynamicBody():
    def __init__(self, origin:tuple[float, float], points:list[Point], springs:list[Spring]):
        self.points = points
        self.springs = springs
    
    def update(self):
        for spring in self.springs:
            spring.relax()
        