from DynamicBody import DynamicBody

class Environment():
    def __init__(self, weight:int, height:int):
        self.weight = weight
        self.height = height

        self.dynamicObjects = list()
    
    def add_dynamic_body(self, obj:DynamicBody):
        self.dynamicObjects.append(obj)

    def update(self):
        for object in self.dynamicObjects:
            object.update()
    
    def draw(self, screen):
        for object in self.dynamicObjects:
            object.draw(screen)