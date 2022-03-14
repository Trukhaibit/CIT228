import sys
import pygame
from winsound import PlaySound

pygame.init()

from settings import Settings
from paddle import Paddle
from ball import Ball
from brick import Brick
from button import Button

class BrickBreaker:

    def __init__(self):
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        size = (self.settings.screen_width, self.settings.screen_height)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Brick Breaker")

        self.paddle = Paddle(self)
        self.ball = Ball(self)
        self.bricks = pygame.sprite.Group()
        self.create_bricks()
        self.play_button = Button(self, "Play")
        self.thud = pygame.mixer.Sound('Brick Breaker/audio/thud.wav')

    def run_game(self):
        self.start_flag = False
        while True:
            for event in pygame.event.get():
                self.key_presses(event)
                if event.type == pygame.QUIT:
                    sys.exit()
            self.set_screen()
    
    def set_screen(self):
        self.screen.fill(self.settings.bg_color)
        if self.start_flag:
            self.font = pygame.font.SysFont(None, 34)
            text = self.font.render("Score: " + str(self.settings.score), 1, self.settings.text_color)
            self.screen.blit(text, (20,10))
            text = self.font.render("Health: " + str(self.settings.health), 1, self.settings.text_color)
            self.screen.blit(text, (1080,10))

            self.paddle.update()
            self.paddle.draw_paddle()

            self.wall_check()
            self.paddle_check()
            self.ball.update()
            self.ball.draw_ball()

            self.check_bricks()
            self.bricks.draw(self.screen)
        else:
            self.play_button.draw_button()

        pygame.display.flip()

        self.clock.tick(60)

    def key_presses(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.paddle.right_flag = True
            elif event.key == pygame.K_LEFT:
                self.paddle.left_flag = True
            elif event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.paddle.right_flag = False
            elif event.key == pygame.K_LEFT:
                self.paddle.left_flag = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked:
                self.start_flag = True

    def wall_check(self):
        if self.ball.rect.x > self.settings.screen_width - self.ball.rect.width:
            self.settings.ball_xSpeed = -self.settings.ball_xSpeed
        if self.ball.rect.x < 0:
            self.settings.ball_xSpeed = -self.settings.ball_xSpeed
        if self.ball.rect.y > self.settings.screen_height - self.ball.rect.height:
            self.settings.ball_ySpeed = -self.settings.ball_ySpeed
            self.settings.health -= 1
            if self.settings.health == 0:
                text = self.font.render("GAME OVER", 1, self.settings.text_color)
                self.screen.blit(text, (550,350))
                pygame.display.flip()
                pygame.time.wait(3000)
                sys.exit()
        if self.ball.rect.y < 0:
            self.settings.ball_ySpeed = -self.settings.ball_ySpeed

    def paddle_check(self):
        paddle_flag = pygame.sprite.collide_rect(self.ball,self.paddle)
        if paddle_flag:
            self.ball.bounce()

    def create_bricks(self):
        for i in range(7):
            brick = Brick(self)
            brick.rect.x = 100 + i* 150
            brick.rect.y = 50
            self.bricks.add(brick)
            self.bricks.draw(self.screen)
        for i in range(7):
            brick = Brick(self)
            brick.rect.x = 100 + i* 150
            brick.rect.y = 120
            self.bricks.add(brick)
            self.bricks.draw(self.screen)
        for i in range(7):
            brick = Brick(self)
            brick.rect.x = 100 + i* 150
            brick.rect.y = 190
            self.bricks.add(brick)
            self.bricks.draw(self.screen)
        for i in range(7):
            brick = Brick(self)
            brick.rect.x = 100 + i* 150
            brick.rect.y = 260
            self.bricks.add(brick)
            self.bricks.draw(self.screen)

    def check_bricks(self):
        dead_bricks = pygame.sprite.spritecollide(self.ball,self.bricks,False)
        for brick in dead_bricks:
            self.ball.bounce()
            self.settings.score += 10
            brick.kill()
            pygame.mixer.Sound.play(self.thud)
            if len(self.bricks)==0:
                text = self.font.render("WINNER!", 1, self.settings.text_color)
                self.screen.blit(text, (550,350))
                pygame.display.flip()
                pygame.time.wait(3000)
                sys.exit

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = BrickBreaker()
    ai.run_game()