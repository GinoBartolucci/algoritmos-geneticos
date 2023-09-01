import pygame
from breakout import Game
from pygame.locals import *
import neat
import os
import pickle
import math


class BreakoutGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height, 6, 6)
        self.paddle = self.game.paddle
        self.ball = self.game.ball
        self.wall = self.game.wall

    def test_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(900)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN and self.game.game_info.game_over:
                    self.game.reset()

            output = net.activate((self.game.game_info.paddle_pos_x,
                                   abs(self.game.game_info.paddle_pos_y -
                                       self.game.game_info.ball_pos_y),
                                   self.game.game_info.ball_pos_x))
            decision = output.index(max(output))
            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(True)
            else:
                self.game.move_paddle(False)
            self.game.loop()
            self.game.draw()

            pygame.display.update()

    def train_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            output = net.activate((self.game.game_info.paddle_pos_x,
                                   abs(self.game.game_info.paddle_pos_y -
                                       self.game.game_info.ball_pos_y),
                                   self.game.game_info.ball_pos_x))
            decision = output.index(max(output))

            valid = True
            if decision == 1:
                valid = self.game.move_paddle(True)
            else:
                valid = self.game.move_paddle(False)
            if not valid:  # Si el movimiento no se puede hacer
                genome.fitness -= 0.001

            self.game.loop()

            self.game.draw()
            pygame.display.update()

            if (self.game.game_info.game_over or self.game.game_info.paddle_hits == 250):
                self.calculate_fitness(
                    genome, self.game.game_info, self.game.rows * self.game.cols)
                break

    def calculate_fitness(self, genome, game_info, blocks):
        p = game_info.points
        h = game_info.paddle_hits
        if p == blocks:
            if h <= p:
                genome.fitness += blocks * abs(p-h)
            elif h > p:
                genome.fitness += blocks - abs(p-h)
        else:
            if h <= p:
                genome.fitness -= (blocks - p + 5)*3
            elif h > p:
                genome.fitness -= ((blocks - p + 5) + abs(p-h))*3

        print(genome.id, "Fitness: ", genome.fitness,
              "Puntos: ", p, "Golpes: ", h)


def test_ai(config):
    with open("proyecto/best.pickle", "rb") as f:
        winner = pickle.load(f)
    width, height = 700, 700
    windows = pygame.display.set_mode((width, height))
    game = BreakoutGame(windows, width, height)
    game.test_ai(winner, config)


def eval_genomes(genomes, config):
    width, height = 700, 600
    windows = pygame.display.set_mode((width, height))
    for genome_id, genome in genomes:
        genome.fitness = 0
        game = BreakoutGame(windows, width, height)
        game.train_ai(genome, config)


def run_neat(config):
    # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-50') #Para empezar desde una generación guardada, hay que comentar neat.Population si hago esto
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(20)) #Guarda data cada 1 generación

    winner = p.run(eval_genomes, 20)  # numero de generaciones
    with open('proyecto/best.pickle', "wb") as f:
        pickle.dump(winner, f)
        print("Guardado")


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    print("Si le das dos veces enter se testea, si le escribis cualquiera se testea se entrena")
    if str(input()) != "":
        run_neat(config)
    else:
        test_ai(config)
pygame.quit()
