import DynamicBody as db

def ReinforcedRectangle(origin:tuple[int, int], width:int, height:int, gap:float):
    points = [db.Point(pos=(origin[0]+w*gap, origin[1]+h*gap)) for h in range(height) for w in range(width)]
    springs = list()
    for h in range(height):
        for w in range(width-1):
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+h*width], s=50, l=gap, d=0.5))
    
    for w in range(width):
        for h in range(height-1):
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+(h+1)*width], s=50, l=gap, d=0.5))
    
    for w in range(width):
        for h in range(1, height):
            if w == 0:
                springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+(h-1)*width], s=50, l=gap*1.4, d=0.5))
                continue
            
            if w == width-1:
                springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w-1+(h-1)*width], s=50, l=gap*1.4, d=0.5))
                continue

            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+(h-1)*width], s=50, l=gap*1.4, d=0.5))
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w-1+(h-1)*width], s=50, l=gap*1.4, d=0.5))
    
    return db.SpringMassBody(points=points, springs=springs)