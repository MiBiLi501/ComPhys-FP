import pygame as pyg

pyg.font.init()
# WINDOW_SIZE = 
screen = pyg.display.set_mode((1000, 600))

screen.fill((255, 255, 255))

clock = pyg.time.Clock()
fps_font = pyg.font.SysFont("Arial", 20)
current_algorithm = "Brute Force"

coord = (100, 50)

running = True
while running:

    # Rendering
    screen.fill((255, 255, 255))
    pyg.draw.circle(surface=screen, color=(0, 0, 255), center=coord, radius=10)
    pyg.display.flip()

    # Update environment
    