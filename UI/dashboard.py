## main load in game

import Core.Config.config
import pygame

from moviepy.video.io.VideoFileClip import VideoFileClip

class dashboard:
    def __init__(self, isClip):
        self._config = Core.Config.config.GameConfig()
        self.height = self._config.get_int_config("screen_resolution","resolution_height")
        self.width = self._config.get_int_config("dash_board","dash_board_width")
        # load wallapper for dashboard
        if not isClip:
            self.image = pygame.image.load("Assets/DashBoardWallPaper/test.jpeg")
            self.image = pygame.transform.scale(image, (self.width, self.height))
            self.image_x = 0 #default
            self.image_y = 0 #default
        else:
            self.clip = VideoFileClip("")


