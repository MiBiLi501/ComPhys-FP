import pygame as pyg
import time
from Environment import Environment
from DynamicBody import *
import Shape
import Settings

pyg.font.init()
# WINDOW_SIZE = 
screen = pyg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

pyg.display.set_caption("Soft Body simulation")

screen.fill((255, 255, 255))

clock = pyg.time.Clock()

coord = (100, 50)

env = Environment(Settings.WIDTH, Settings.HEIGHT)
env.add_dynamic_body(Shape.ReinforcedTriangle(origin=(300, -700), length=5, gap=50, stiffness=70, damping=10))

cur = time.time()
prev = cur

running = True


freeze = False


gray = (128, 128, 128)
transparent_gray = (255, 255, 255, 128)  

sidebar_width = int(Settings.WIDTH * 0.2)
sidebar = pyg.Surface((sidebar_width, Settings.HEIGHT)) # Adjusted to HEIGHT instead of WIDTH
sidebar.fill(gray)

font = pyg.font.SysFont(None, 36)
font = pyg.font.SysFont("Arial", 28)

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            if pause_button_rect.collidepoint(event.pos):
                freeze = not freeze

            elif env.check_select(*event.pos):
                print(*event.pos)
        elif event.type == pyg.MOUSEBUTTONUP:
            if env.get_select(): env.reset_select()
        
        elif event.type == pyg.MOUSEMOTION:
            if env.get_select():
                env.get_select().set_curPos(event.pos)


    if not freeze:  
        # while (cur - prev < 1 / 60):
        #     cur = time.time()
        env.update()

    
    screen.fill((255, 255, 255))  

    pause_button_text = font.render("Freeze", True, (255, 255, 255))
    pause_button_rect = pause_button_text.get_rect(topleft=(10, 10))
    pyg.draw.rect(screen, (0, 0, 0), pause_button_rect)  
    screen.blit(pause_button_text, pause_button_rect)  

    
    env.draw(screen)

    if freeze:
        
        env.update_springs()
        overlay = pyg.Surface((screen.get_width(), screen.get_height()), pyg.SRCALPHA)
        overlay.fill((255, 255, 255, 128)) 
        screen.blit(overlay, (0, 0))

        
        text = font.render("freeze", True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)

    screen.blit(sidebar, (Settings.WIDTH - sidebar_width, 0)) # Adjusted sidebar position
    input_editor_text = font.render("Input Editor", True, (255, 255, 255)) # Added text for Input Editor
    sidebar.blit(input_editor_text, (10, 10)) # Added blitting text onto the sidebar
    pyg.display.flip()
