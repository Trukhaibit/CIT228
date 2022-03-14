import pygame
from pygame.sprite import Sprite
BLACK = (255,255,255)
class Paddle(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.right_flag = False
        self.left_flag = False

        self.image=pygame.image.load('Brick Breaker/images/paddle.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.paddle_x
        self.rect.y = self.settings.paddle_y
 
    def update(self):
        if (self.right_flag == True):
            self.rect.x += self.settings.paddle_speed
            if self.rect.x > self.settings.screen_width - self.rect.width:
                self.rect.x = self.settings.screen_width - self.rect.width
        elif (self.left_flag == True):
            self.rect.x -= self.settings.paddle_speed
            if self.rect.x < 0:
                self.rect.x = 0

    def draw_paddle(self):
        self.screen.blit(self.image, self.rect)
