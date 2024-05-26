from DynamicBody import SpringMassBody

class Environment():
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

        self.dynamicObjects:list[SpringMassBody] = list()
    
    def add_dynamic_body(self, obj:SpringMassBody):
        self.dynamicObjects.append(obj)

    def update(self):
        for object in self.dynamicObjects:
            object.update()
    
    def draw(self, screen):
        for object in self.dynamicObjects:
            object.draw(screen)