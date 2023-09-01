import pygame


class Wall():
    BLUE = (69, 160, 215)

    def __init__(self, window_width, rows, cols, bg_color):
        self.width = window_width // cols
        self.height = 50
        self.rows = rows
        self.cols = cols
        self.bg_color = bg_color
        self.reset()

    def create_wall(self):
        self.blocks = []
        for row in range(self.rows):
            # reset the block row list
            block_row = []
            # iterate through each column in that row
            for col in range(self.cols):
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

    def draw_wall(self, window):
        for row in self.blocks:
            for block in row:
                pygame.draw.rect(window, self.BLUE, block)
                pygame.draw.rect(window, self.bg_color, block, 2)

    def reset(self):
        self.create_wall()
