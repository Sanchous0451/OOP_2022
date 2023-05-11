import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 200
screen = pygame.display.set_mode((800, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
class Ball:
    def __init__(self, screen, x, y, radius, color, speed, lifetime):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.lifetime = lifetime

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def update(self):
        self.x += self.speed[0]
        self.y += self.speed[1]

        
        if self.x - self.radius < 0 or self.x + self.radius > 800:
            self.speed[0] = -self.speed[0]
        if self.y - self.radius < 0 or self.y + self.radius > 600:
            self.speed[1] = -self.speed[1]

        self.lifetime -= 1
        return self.lifetime > 0

class Game:
    def __init__(self):
        self.score = 0
        self.balls = []
        self.screen = pygame.display.set_mode((800, 600))
        self.started = False

    def restart(self):
        self.score = 0
        self.balls = []
        self.started = False


    def new_ball(self):
        radius = randint(30, 50)
        x = randint(10 + randint(20,60), 800 - randint(20,60))
        y = randint(10 + randint(20,60), 600 - randint(20,60))
        color = COLORS[randint(0, 5)]
        speed = [randint(-1, 2), randint(-1, 2)]
        ball = Ball(self.screen, x, y, radius, color, speed, 600)
        self.balls.append(ball)

    def delete_ball(self, ball):
        self.balls.remove(ball)

    def check_click(self, x, y):
        for ball in self.balls:
            if (x - ball.x) ** 2 + (y - ball.y) ** 2 <= ball.radius ** 2:
                self.delete_ball(ball)
                self.score += 1
                return

    def game_loop(self):
        finished = False
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        while not finished:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.started:
                        self.started = True
                    self.check_click(*event.pos)

    

            if randint(1, 90) == 1:
                self.new_ball()

            self.screen.fill(BLACK)

            for ball in self.balls:
                if not ball.update():
                    self.delete_ball(ball)

            for ball in self.balls:
                ball.draw()

            text = font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(text, (10, 10))

        
            pygame.display.update()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.game_loop()