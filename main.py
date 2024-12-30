import sys
import pygame
import Core.Config.config
import Core.Controller.game_controller

# Initialize Pygame
pygame.init()

# set up 
config = Core.Config.config.GameConfig()

window = pygame.display.set_mode((config.get_int_config("screen_resolution","resolution_width"),
                                  config.get_int_config("screen_resolution","resolution_height")))

game_controller = Core.Controller.game_controller.GameController(window)

pygame.display.set_caption("The Tatician")

def start_program(game_controller):
    running = True
    while running:
        game_controller.draw_dashboard(None)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

# Set up display
    
# Game
start_program(game_controller)

# Quit Pygame
pygame.quit()
sys.exit()



