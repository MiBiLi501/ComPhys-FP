class Spring():
    def __init__(self, obj1, obj2, s:float, l:float, d:float) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.stiffness = s
        self.length = l
        self.damping = d
    
    def relax(self):
        ...