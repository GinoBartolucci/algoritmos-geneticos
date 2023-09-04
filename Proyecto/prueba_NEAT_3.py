import pygame
from breakout import Game
from pygame.locals import *
import neat
import os
import pickle

fitness_list = []
game_list = []
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
            clock.tick(140)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            output = net.activate((self.game.game_info.paddle_pos_x,abs(self.game.game_info.paddle_pos_y-self.game.game_info.ball_pos_y),self.game.game_info.ball_pos_x))
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
            
            if (self.game.game_info.game_over):
                if (self.game.game_info.points == 36): game_list.append(1)
                else: game_list.append(0)
                break

    def train_ai(self, genome, config):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            output = net.activate((self.game.game_info.paddle_pos_x,abs(self.game.game_info.paddle_pos_y-self.game.game_info.ball_pos_y),self.game.game_info.ball_pos_x))
            decision = output.index(max(output))
            if decision == 0:
                pass
            if decision == 1:
                self.game.move_paddle(True)
            else:
                self.game.move_paddle(False)
            self.game.loop()
            self.game.draw()
            pygame.display.update()

            if (self.game.game_info.game_over):
                self.calculate_fitness(
                    genome, self.game.game_info)
                break

    def calculate_fitness(self, genome, game_info):
        if game_info.points == self.game.rows*self.game.cols:
            genome.fitness += 50 - game_info.paddle_hits/10
        else: genome.fitness += game_info.points

def test_ai(config):
    with open("best.pickle30", "rb") as f:
        winner = pickle.load(f)
    width, height = 700, 700
    windows = pygame.display.set_mode((width, height))
    game = BreakoutGame(windows, width, height)
    game.test_ai(winner, config)


def eval_genomes(genomes, config):
    width, height = 700, 700
    windows = pygame.display.set_mode((width, height))
    gen = []
    for genome_id, genome in genomes:
        genome.fitness = 0
        game = BreakoutGame(windows, width, height)
        game.train_ai(genome, config)
        gen.append(genome.fitness)
    fitness_list.append(gen)


def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-8') #Para empezar desde una generación guardada, hay que comentar neat.Population si hago esto
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(10)) #Guarda checkpoint cada 1 generación

    winner = p.run(eval_genomes, 30)  # numero de generaciones
    with open('best.pickle30', "wb") as f:
        pickle.dump(winner, f)
        print(fitness_list)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    test_ai(config)     # Testear el best.pickle
    #run_neat(config)   # Entrenar y generar best pickle
pygame.quit()
