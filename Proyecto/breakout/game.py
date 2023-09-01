from .paddle import Paddle
from .ball import Ball
from .wall import Wall
import pygame

pygame.init()


class GameInfo:
    def __init__(self, game_over, points, paddle_hits, ball_pos_x, ball_pos_y, paddle_pos_x, paddle_pos_y):
        self.points = points
        self.ball_pos_x = ball_pos_x
        self.ball_pos_y = ball_pos_y
        self.paddle_pos_x = paddle_pos_x
        self.paddle_pos_y = paddle_pos_y
        self.paddle_hits = paddle_hits
        self.game_over = game_over


class Game:
    BG_COLOR = (218, 200, 170)
    SCORE_FONT = pygame.font.SysFont("comicsans", 50)
    RED = (255, 0, 0)

    def __init__(self, window, window_width, window_height, cols, rows):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height
        self.cols = cols
        self.rows = rows
        self.paddle = Paddle(self.window_width / 2 - Paddle.WIDTH / 2,
                             self.window_height - Paddle.HEIGHT * 2)
        self.ball = Ball(self.paddle.rect.x + (self.paddle.WIDTH //
                         2), self.paddle.rect.y - 1 - self.paddle.HEIGHT)
        self.wall = Wall(self.window_width, self.cols,
                         self.rows, self.BG_COLOR)

        self.game_info = GameInfo(False, 0, 0, self.ball.rect.x,
                                  self.ball.rect.y, self.paddle.rect.x + self.paddle.WIDTH/2, self.paddle.rect.y)
        self.game_info.ball_pos_y = self.paddle.rect.y
        self.destroyed_blocks = 0
        self.collision_thresh = 12

    def _draw_hits(self):
        hits_text = self.SCORE_FONT.render(
            f"{self.destroyed_blocks}", 1, self.RED)
        self.window.blit(hits_text, (self.window_width //
                                     2 - hits_text.get_width()//2, 10))

    def _blocks_collision(self):
        # collision threshold
        row_count = 0
        for row in self.wall.blocks:
            item_count = 0
            for item in row:
                # check collision
                if self.ball.rect.colliderect(item):
                    # check if collision was from above
                    if abs(self.ball.rect.bottom - item.top) < self.collision_thresh and self.ball.vel_y > 0:
                        self.ball.vel_y *= -1
                    # check if collision was from below
                    if abs(self.ball.rect.top - item.bottom) < self.collision_thresh and self.ball.vel_y < 0:
                        self.ball.vel_y *= -1
                    # check if collision was from left
                    if abs(self.ball.rect.right - item.left) < self.collision_thresh and self.ball.vel_x > 0:
                        self.ball.vel_x *= -1
                    # check if collision was from right
                    if abs(self.ball.rect.left - item.right) < self.collision_thresh and self.ball.vel_x < 0:
                        self.ball.vel_x *= -1
                    # damage the block
                    self.wall.blocks[row_count][item_count] = (0, 0, 0, 0)
                    self.destroyed_blocks += 1
                    self.ball.increase_vel(1.015)
                # increase item counter
                item_count += 1
            # increase row counter
            row_count += 1
            self.game_info.points = self.destroyed_blocks

    def _window_collision(self):
        # check for collision with walls
        if self.ball.rect.left < 0 or self.ball.rect.right > self.window_width:
            self.ball.vel_x *= -1
        if self.ball.rect.top < 0:
            self.ball.vel_y *= -1

    def _paddle_collision(self):
        # look for collission with paddle
        if self.ball.rect.colliderect(self.paddle):
            # check if colliding from the top
            if abs(self.ball.rect.bottom - self.paddle.rect.top) < self.collision_thresh and self.ball.vel_y > 0:
                self.ball.vel_y *= -1
                self.game_info.paddle_hits += 1
            else:
                self.ball.vel_x *= -1

    def draw(self):
        self.window.fill(self.BG_COLOR)
        self.paddle.draw(self.window)
        self.ball.draw(self.window)
        self.wall.draw_wall(self.window)
        self._draw_hits()

    def move_paddle(self, left):
        if left and (self.paddle.rect.x - self.paddle.SPEED) < 0:
            return False
        if not left and (self.paddle.rect.x + self.paddle.WIDTH + self.paddle.SPEED) > self.window_width:
            return False
        self.paddle.move(left)
        self.game_info.paddle_pos_x = (
            self.paddle.rect.x + self.paddle.WIDTH/2)
        return True

    def reset(self):
        self.paddle.reset()
        self.ball.reset()
        self.wall.reset()
        self.game_info = GameInfo(False, 0, 0, self.ball.rect.x,
                                  self.ball.rect.y, self.paddle.rect.x + self.paddle.WIDTH/2, self.paddle.rect.y)
        self.destroyed_blocks = 0

    def loop(self):
        if not self.game_info.game_over:
            self.ball.move()
            self.game_info.ball_pos_x = self.ball.rect.x
            self.game_info.ball_pos_y = self.ball.rect.y
            self._blocks_collision()
            self._window_collision()
            self._paddle_collision()

            if ( (self.ball.rect.bottom > self.window_height) or (self.game_info.paddle_hits >= 250) ):
                self.game_info.game_over = True  # lose

            if self.game_info.points == (self.wall.cols * self.wall.rows):
                self.game_info.game_over = True  # win

            return self.game_info
        else:
            return self.game_info
