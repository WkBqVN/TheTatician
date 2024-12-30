#game controller

import pygame

class GameController:
    '''
    game controller manager mode and something not belong to the match
    '''
    def __init__(self,window):
        self.window = window
        return

    def load_screen(self):    
        return

    # same height with window or screen
    def draw_dashboard(self,dashboard,isClip):
        clock = pygame.time.Clock()
        if not isClip:
            self.window.blit(dashboard,(dashboard.image_x,dashboard.image_y))
        else:
            for frame in dashboard.clip.iter_frames(fps=30, with_times=False):
            # Chuyển frame thành bề mặt Pygame
                frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
                self.window.blit(frame_surface, (0, 0))
                pygame.display.update()
                # Giới hạn FPS
                clock.tick(30)

    def load_left_panel(self):
        return

    


    

