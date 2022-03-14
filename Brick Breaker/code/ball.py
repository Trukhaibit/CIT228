import pygame
from pygame.sprite import Sprite
 
class Ball(Sprite):
    
    def __init__(self, ai_game):
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen

        self.image=pygame.image.load('Brick Breaker/images/ball.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.ball_x
        self.rect.y = self.settings.ball_y
        
    def update(self):
        self.rect.x += self.settings.ball_xSpeed
        self.rect.y += self.settings.ball_ySpeed
    
    def bounce(self):
        self.settings.ball_ySpeed = -self.settings.ball_ySpeed
        
    def draw_ball(self):
        self.screen.blit(self.image, self.rect)