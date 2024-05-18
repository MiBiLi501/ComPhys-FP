class Environment():
    def __init__(self, weight:int, height:int):
        self.weight = weight
        self.height = height

        self.dynamicObjects = list()
        self.staticObjects = list()
    
    def update(self):
        for object in self.dynamicObjects:
            object.update()