import pygame as pyg
import time
from Environment import Environment
from DynamicBody import *
import GUI
import Shape
import Settings

pyg.font.init()

screen = pyg.display.set_mode((Settings.WIDTH, Settings.HEIGHT))

pyg.display.set_caption("Soft Body simulation")

screen.fill((255, 255, 255))

clock = pyg.time.Clock()

coord = (100, 50)

env = Environment(Settings.WIDTH, Settings.HEIGHT)

cur = time.time()
prev = cur

running = True


freeze = False

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
        
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_a:
                GUI.add_shape_prompt(env=env)
            
            if event.key == pyg.K_r:
                GUI.reset_env_prompt(env=env)
                
                


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

    input_editor_text = font.render("Input Editor", True, (255, 255, 255)) # Added text for Input Editor
    pyg.display.flip()
