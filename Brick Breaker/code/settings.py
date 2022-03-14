class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800

        self.bg_color = (12, 30, 63)
        self.text_color = (255, 255, 255)

        self.score = 0
        self.health = 3

        self.paddle_x = 350
        self.paddle_y = 700
        self.paddle_color = (255, 255, 255)
        self.paddle_speed = 5

        self.ball_x = 350
        self.ball_y = 500
        self.ball_xSpeed = -5
        self.ball_ySpeed = -7
        