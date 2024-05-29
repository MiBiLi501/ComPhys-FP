import DynamicBody as db
import random

def ReinforcedRectangle(origin:tuple[int, int], width:int, height:int, gap:float, stiffness:float, damping:float):
    width += 1
    height += 1
    points = [db.Point(pos=(origin[0]+w*gap+random.randint(0, 10), origin[1]+h*gap)) for h in range(height) for w in range(width)]
    springs = list()
    for h in range(height):
        for w in range(width-1):
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+h*width], s=stiffness, l=gap, d=damping))
    
    for w in range(width):
        for h in range(height-1):
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+(h+1)*width], s=stiffness, l=gap, d=damping))
    
    for w in range(width):
        for h in range(1, height):
            if w == 0:
                springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+(h-1)*width], s=stiffness, l=gap*1.41, d=damping))
                continue
            
            if w == width-1:
                springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w-1+(h-1)*width], s=stiffness, l=gap*1.41, d=damping))
                continue

            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w+1+(h-1)*width], s=stiffness, l=gap*1.41, d=damping))
            springs.append(db.Spring(obj1=points[w+h*width], obj2=points[w-1+(h-1)*width], s=stiffness, l=gap*1.41, d=damping))
    
    return db.SpringMassBody(points=points, springs=springs)

def ReinforcedTriangle(origin:tuple[int, int], length:int, gap:float, stiffness:float, damping:float):
    length += 1
    points = [db.Point(pos=(origin[0]-y*gap/2+x*gap, origin[1]+y*gap*0.866)) for y in range(length) for x in range(y+1)]
    springs = list()

    for y in range(length):
        for x in range(y+1):
            if y < length-1:
                springs.append(db.Spring(obj1=points[y*(y+1)//2+x], obj2=points[(y+2)*(y+1)//2+x], s=stiffness, l=gap, d=damping))
                springs.append(db.Spring(obj1=points[y*(y+1)//2+x], obj2=points[(y+2)*(y+1)//2+x+1], s=stiffness, l=gap, d=damping))
            
            if x < y:
                springs.append(db.Spring(obj1=points[y*(y+1)//2+x], obj2=points[(y)*(y+1)//2+x+1], s=stiffness, l=gap, d=damping))


    return db.SpringMassBody(points=points, springs=springs)
