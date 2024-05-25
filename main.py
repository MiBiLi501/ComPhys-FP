import pygame as pyg
import time

from Environment import Environment
from DynamicBody import *

pyg.font.init()
# WINDOW_SIZE = 
screen = pyg.display.set_mode((1000, 600))

pyg.display.set_caption("Soft Body simulation")

screen.fill((255, 255, 255))

clock = pyg.time.Clock()

coord = (100, 50)

env = Environment(1000, 600)

p1, p2, p3 = Point(pos=(200, 200)), Point(pos=(200, 400)), Point(pos=(300, 200))
body = SpringMassBody(origin=(200, 200), points=[p1, p2, p3], springs=[Spring(obj1=p1, obj2=p2, s=1, l=100, d=0.5), Spring(obj1=p1, obj2=p3, s=1, l=100, d=0.1), Spring(obj1=p2, obj2=p3, s=1, l=100, d=0.1)])

p4, p5, p6 = Point(pos=(600, 200)), Point(pos=(270, 600)), Point(pos=(600, 500))
body2 = SpringMassBody(origin=(200, 200), points=[p4, p5, p6], springs=[Spring(obj1=p5, obj2=p6, s=1, l=100, d=0.1), Spring(obj1=p4, obj2=p6, s=1, l=100, d=0.1)])

env.add_dynamic_body(body)
env.add_dynamic_body(body2)

cur = time.time()
prev = cur

running = True


paused = False


gray = (128, 128, 128)
transparent_gray = (255, 255, 255, 128)  


font = pyg.font.SysFont(None, 36)

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            if pause_button_rect.collidepoint(event.pos):
                paused = not paused  

    if not paused:  
        while (cur - prev < 1 / 60):
            cur = time.time()

        
        env.update()

    
    screen.fill((255, 255, 255))  

    pause_button_text = font.render("Pause", True, (255, 255, 255))
    pause_button_rect = pause_button_text.get_rect(topleft=(10, 10))
    pyg.draw.rect(screen, (0, 0, 0), pause_button_rect)  
    screen.blit(pause_button_text, pause_button_rect)  

    
    env.draw(screen)

    if paused:
        
        overlay = pyg.Surface((screen.get_width(), screen.get_height()), pyg.SRCALPHA)
        overlay.fill((255, 255, 255, 128)) 
        screen.blit(overlay, (0, 0))  

        
        text = font.render("PAUSED", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

    pyg.display.flip()
