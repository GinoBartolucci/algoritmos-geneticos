import pygame
from breakout import Game
from pygame.locals import *
import neat
import os 

class BreakoutGame:
    def __init__(self, window, width, height):
        self.game = Game(window,width,height, 6, 6)
        self.paddle = self.game.paddle
        self.ball = self.game.ball
        self.wall = self.game.wall
        
    def test_ai(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.game.move_paddle( left = True )
            if keys[pygame.K_RIGHT]:
                self.game.move_paddle( left = False )
            
            self.game.loop()
            self.game.draw()
            pygame.display.update()
            
    def train_ai(self, genome, config):
        clock = pygame.time.Clock()
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        run = True
        while run:
            clock.tick(1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            output = net.activate((self.paddle.rect.x, self.ball.rect.y, abs(self.paddle.rect.y-self.ball.rect.y), self.ball.rect.x))
            decision = output.index(max(output))
            
            if decision == 0:
                pass
            elif decision == 1:
                self.game.move_paddle(True)
            else:
                self.game.move_paddle(False)
            
            game_info = self.game.loop()
            
            self.game.draw()
            pygame.display.update()
            
            if (self.game.game_info.game_over):
                self.calculate_fitness(genome, game_info, self.game.destroyed_blocks)
                break
    
    def calculate_fitness(self, genome, game_info,destroyed_blocks):
        genome.fitness += game_info.paddle_hits
        genome.fitness += destroyed_blocks*0.5
            
def eval_genomes(genomes, config):
    width, height = 700, 700
    windows = pygame.display.set_mode((width, height))
    for genome_id, genome in genomes:
        genome.fitness = 0
        game = BreakoutGame(windows, width, height)
        game.train_ai(genome, config)
        
            
def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-19') #Para empezar desde una generación guardada, hay que comentar neat.Population si hago esto
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(1)) #Guarda data cada 1 generación
    
    winner = p.run(eval_genomes, 50)
    
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    
    run_neat(config)





pygame.quit()