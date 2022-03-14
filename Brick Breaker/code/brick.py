import pygame

class Brick(pygame.sprite.Sprite):
    #This class represents a brick. It derives from the "Sprite" class in Pygame.
 
    def __init__(self, ai_game):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.settings
 
        self.image=pygame.image.load('Brick Breaker/images/brick.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.settings.ball_x
        self.rect.y = self.settings.ball_y

    def draw_brick(self):
        self.screen.blit(self.image, self.rect)