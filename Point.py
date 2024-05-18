import numpy as np

class Point():
    def __init__(self,pos:tuple[float, float], mass:float):
        self.current = np.array(pos)
        self.velocity = np.zeros(2)
        self.force = np.zeros(2)
        self.radius = 5
