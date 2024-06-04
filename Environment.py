from DynamicBody import SpringMassBody, Point

class Environment():
    def __init__(self, width:int, height:int):
        self.width = width
        self.height = height

        self.selected:None|Point = None

        self.dynamicObjects:list[SpringMassBody] = list()

        self.points:list[Point] = list()
    
    def add_dynamic_body(self, obj:SpringMassBody):
        self.dynamicObjects.append(obj)
        for point in obj.points:
            self.points.append(point)
    
    def check_select(self, x:int, y:int):
        if self.selected: return False

        for point in self.points:
            if((point.curPos[0]-x)**2+(point.curPos[1]-y)**2 <= point.radius):
                self.selected = point
                point.set_static(True)
                return True
        
        return False
    
    def get_select(self):
        return self.selected

    def reset_select(self):
        self.selected.set_static(False)
        self.selected = None

    def update(self):
        for object in self.dynamicObjects:
            object.update()
    
    def update_springs(self):
        for object in self.dynamicObjects:
            object.update_springs()        
    
    def draw(self, screen):
        for object in self.dynamicObjects:
            object.draw(screen)