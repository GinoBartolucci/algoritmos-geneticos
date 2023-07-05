import pygame
import random

# Dimensiones de la ventana del juego
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Dimensiones de la paleta y los bloques
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 20
BLOCK_MARGIN = 4
BLOCK_COLUMNS = 6
BLOCK_ROWS = 5

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializar pygame
pygame.init()

# Crear la ventana del juego
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Breakout")

clock = pygame.time.Clock()

# Clase para representar la paleta
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PADDLE_WIDTH, PADDLE_HEIGHT])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = (WINDOW_WIDTH - PADDLE_WIDTH) // 2
        self.rect.y = WINDOW_HEIGHT - PADDLE_HEIGHT

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > WINDOW_WIDTH - PADDLE_WIDTH:
            self.rect.x = WINDOW_WIDTH - PADDLE_WIDTH

# Clase para representar los bloques
class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BLOCK_WIDTH, BLOCK_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Función para generar los bloques
def generate_blocks():
    blocks = pygame.sprite.Group()
    block_width_total = (BLOCK_WIDTH + BLOCK_MARGIN) * BLOCK_COLUMNS - BLOCK_MARGIN
    x_offset = (WINDOW_WIDTH - block_width_total) // 2 + BLOCK_MARGIN
    y_offset = 120
    for row in range(BLOCK_ROWS):
        for column in range(BLOCK_COLUMNS):
            x = x_offset + (BLOCK_WIDTH + BLOCK_MARGIN) * column
            y = y_offset + (BLOCK_HEIGHT + BLOCK_MARGIN) * row
            block = Block(x, y)
            blocks.add(block)
    return blocks

# Clase para representar la pelota
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = (WINDOW_WIDTH - 10) // 2
        self.rect.y = (WINDOW_HEIGHT - 10) // 2
        self.speed_x = random.choice([-3, 3])
        self.speed_y = -3

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0 or self.rect.x >= WINDOW_WIDTH - 10:
            self.speed_x *= -1        
        if self.rect.y <= 0:
            self.speed_y *= -1
        elif self.rect.y >= WINDOW_HEIGHT - 10:
            # Reiniciar la posición de la pelota si se pierde
            self.rect.x = (WINDOW_WIDTH - 10) // 2
            self.rect.y = (WINDOW_HEIGHT - 10) // 2
            self.speed_y = -3

# Inicializar paleta, bloques y pelota
all_sprites = pygame.sprite.Group()
paddle = Paddle()
all_sprites.add(paddle)
blocks = generate_blocks()
all_sprites.add(blocks)
ball = Ball()
all_sprites.add(ball)

# Variable para llevar la puntuación
score = 0

# Fuente para el contador
font = pygame.font.Font(None, 36)

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar la paleta, bloques y pelota
    all_sprites.update()

    # Detectar colisiones con la paleta
    if pygame.sprite.collide_rect(ball, paddle):
        ball.speed_y *= -1

    # Detectar colisiones con los bloques
    collisions = pygame.sprite.spritecollide(ball, blocks, True)
    for block in collisions:
        score += 1
        ball.speed_y *= -1

    # Dibujar la ventana del juego
    window.fill(BLACK)
    all_sprites.draw(window)

    # Mostrar el contador en la ventana
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    pygame.display.flip()

    # Controlar la velocidad de actualización del juego
    clock.tick(60)

# Cerrar pygame
pygame.quit()