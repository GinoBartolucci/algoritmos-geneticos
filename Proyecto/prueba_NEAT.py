import pygame
from pygame.locals import *
import random

import neat
import pickle
import math
import os

pygame.init()

screen_width = 600
screen_height = 600
# define game variables
cols = 6
rows = 6
clock = pygame.time.Clock()
fps = 240
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout')

# define colours
bg = (218, 200, 170)
red = (242, 85, 96)
blue = (69, 160, 215)
black_red = (220, 60, 70)
# font
font = pygame.font.Font(None, 36)


class wall():
    def __init__(self):
        self.width = screen_width // cols
        self.height = 50
        self.reset()

    def create_wall(self):
        self.blocks = []
        for row in range(rows):
            # reset the block row list
            block_row = []
            # iterate through each column in that row
            for col in range(cols):
                # generate x and y positions for each block and create a rectangle from that
                block_x = col * self.width
                block_y = row * self.height
                block_individual = pygame.Rect(
                    block_x, block_y, self.width, self.height)
                # create a list at this point to store the rect and colour data
                # append that individual block to the block row
                block_row.append(block_individual)
            # append the row to the full list of blocks
            self.blocks.append(block_row)

    def draw_wall(self):
        for row in self.blocks:
            for block in row:
                pygame.draw.rect(screen, blue, block)
                pygame.draw.rect(screen, bg, block, 2)

    def reset(self):
        self.create_wall()


class paddle():
    def __init__(self):
        self.reset()

    def move(self, left=False):
        # Return true
        if left and self.rect.left > 0:
            self.rect.x -= self.speed
            return True
        elif not left and self.rect.right < screen_width:
            self.rect.x += self.speed
            return True
        return False

    def draw(self):
        pygame.draw.rect(screen, red, self.rect)
        pygame.draw.rect(screen, black_red, self.rect, 3)

    def reset(self):
        # define paddle variables
        self.height = 20
        self.width = int(screen_width / cols)
        self.x = int((screen_width / 2) - (self.width / 2))
        self.y = screen_height - (self.height * 2)
        self.speed = 8
        self.rect = Rect(self.x, self.y, self.width, self.height)


class game_info():
    def __init__(self):
        self.reset()

    def displayInfo(self):
        if self.points != -1:  # wining
            score_text = font.render("Score: " + str(self.points) + "\n Vx: %.2f" %
                                     self.vel_x + "  Vy: %.2f" % self.vel_y, True, red)
        elif self.points == -1:  # lose
            score_text = font.render("Losse", True, red)
        x = 0  # int((screen_width / 2))
        y = screen_height - 30  # screen_height - 200
        screen.blit(score_text, (x, y))

    def reset(self):
        self.points = 0
        self.vel_x = 0.0
        self.vel_y = 0.0
        self.pos_x = 0.0
        self.pos_y = 0.0
        self.displayInfo()


class game_ball():
    def __init__(self, x, y):
        self.reset(x, y)

    def move(self):
        # collision threshold
        collision_thresh = 6
        # start off with the assumption that the wall has been destroyed completely
        row_count = 0
        for row in wall.blocks:
            item_count = 0
            for item in row:
                # check collision
                if self.rect.colliderect(item):
                    # check if collision was from above
                    if abs(self.rect.bottom - item.top) < collision_thresh and self.speed_y > 0:
                        self.speed_y *= -1
                    # check if collision was from below
                    if abs(self.rect.top - item.bottom) < collision_thresh and self.speed_y < 0:
                        self.speed_y *= -1
                    # check if collision was from left
                    if abs(self.rect.right - item.left) < collision_thresh and self.speed_x > 0:
                        self.speed_x *= -1
                    # check if collision was from right
                    if abs(self.rect.left - item.right) < collision_thresh and self.speed_x < 0:
                        self.speed_x *= -1
                    # damage the block
                    wall.blocks[row_count][item_count] = (0, 0, 0, 0)
                    self.destroyed += 1
                    self.speed_x *= 1.01
                    self.speed_y *= 1.01
                # check if block still exists, in whcih case the wall is not destroyed
                # if wall.blocks[row_count][item_count][0] != (0, 0, 0, 0):
                    # wall_destroyed = 0
                # increase item counter
                item_count += 1
            # increase row counter
            row_count += 1

        # check for collision with walls
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.speed_x *= -1

        # check for collision with top and bottom of the screen
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > screen_height:
            self.destroyed = -1  # lose

        # look for collission with paddle
        if self.rect.colliderect(player_paddle):
            # check if colliding from the top
            if abs(self.rect.bottom - player_paddle.rect.top) < collision_thresh and self.speed_y > 0:
                self.speed_y *= -1
            else:
                self.speed_x *= -1

        # mover la bocha
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        game_info.points = self.destroyed  # Actualiza el puntaje
        game_info.vel_x = self.speed_x
        game_info.vel_y = self.speed_y
        game_info.pos_x = self.rect.x
        game_info.pos_y = self.rect.y
        game_info.displayInfo()

    def draw(self):
        pygame.draw.circle(screen, red, (self.rect.x + self.ball_rad,
                           self.rect.y + self.ball_rad), self.ball_rad)
        pygame.draw.circle(screen, black_red, (self.rect.x + self.ball_rad,
                           self.rect.y + self.ball_rad), self.ball_rad, 3)

    def reset(self, x, y):
        self.destroyed = 0
        self.ball_rad = 10
        self.x = x - self.ball_rad
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        velx = [1.7, 1.8, 1.9, 2, 2.1, 2.2, 2.3]
        dirx = [-1, 1]
        self.speed_x = ((random.choice(velx)**2) * random.choice(dirx))
        # velocidad 6 = sqrt(speed_x^2 + speed_y^2)
        # speed_y = sqrt(speed_x^2 + speed_y^2)
        vely = math.sqrt(16 - abs(self.speed_x))
        self.speed_y = -1 * vely
        game_info.vel_x = self.speed_x
        game_info.vel_y = self.speed_y


wall = wall()
player_paddle = paddle()
game_info = game_info()
ball = game_ball(player_paddle.x + (player_paddle.width // 2),
                 player_paddle.y - player_paddle.height)


def loop():
    run = True
    live_ball = False
    while run:
        clock.tick(fps)
        screen.fill(bg)
        # draw all objects
        wall.draw_wall()
        player_paddle.draw()
        ball.draw()

        if live_ball:
            # Mover paddle
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                player_paddle.move(left=True)
            if key[pygame.K_RIGHT]:
                player_paddle.move(left=False)
            # Coliciones
            ball.move()  # -->Actualiza game info
            if game_info.points == (cols * rows):  # win
                live_ball = False
            elif game_info.points == -1:  # lose
                live_ball = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:  # si perde espera el click para reiniciar
                live_ball = True
                ball.reset(player_paddle.x + (player_paddle.width //
                           2), player_paddle.y - player_paddle.height)
                player_paddle.reset()
                game_info.reset()
                wall.reset()

        pygame.display.update()

    pygame.quit()



def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        # crea una net para cada genoma
        # esta red se le pasa los parametros de entrada y devuelve la salida
        # dependiendo de esa salida mueve el paddle
        # dependiendo de si se movio bien o no ajusta el fitness
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = 0
        # setea para cada genoma
        ball.reset(player_paddle.x + (player_paddle.width // 2),
                   player_paddle.y - player_paddle.height)
        player_paddle.reset()
        game_info.reset()
        wall.reset()
        # corre el juego y entrena el genoma cambiando el fitness
        run = True
        live_ball = True
        points = 0
        while run:
            clock.tick(fps)
            screen.fill(bg)
            # draw all objects
            wall.draw_wall()
            player_paddle.draw()
            ball.draw()

            if live_ball:
                # con net.activate le pasamos los inputs y nos devuelve la salida
                output = net.activate(
                    [game_info.vel_x, game_info.vel_y, game_info.pos_x, game_info.pos_y, player_paddle.rect.x])
                decision = output.index(max(output))

                ball.move()  # -->Actualiza game info

                valid = True
                if decision == 0:  # que se mueva
                    genome.fitness -= 0.01
                elif decision == 1:  # mover derecha
                    valid = player_paddle.move(left=False)
                else:  # mover izquierda
                    valid = player_paddle.move(left=True)
                if not valid:  # Si el movimiento no se puede hacer
                    genome.fitness -= 1

                # Coliciones
                if game_info.points > points:  # rompio un bloque
                    genome.fitness += 1
                    points = game_info.points
                if game_info.points == (cols * rows):  # win
                    genome.fitness += 1
                    live_ball = False
                    break  # termina el juego
                elif game_info.points == -1:  # lose
                    genome.fitness -= 1
                    live_ball = False
                    break  # termina el juego

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-85')
    # genera la poblacion en base a la configuracion que definimos
    p = neat.Population(config)
    # Ver detalles de la generaciones a medida que pasan
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(1))

    # Pasamos la funcion que se encarga de evaluar los genomas (Fitness)
    winner = p.run(eval_genomes, 50)  # cuando un genoma llega a
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    run_neat(config)
    # test_best_network(config)
