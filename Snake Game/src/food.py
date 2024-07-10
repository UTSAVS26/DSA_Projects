import pygame
import random
from src.settings import WHITE, SNAKE_BLOCK, WIDTH, HEIGHT

class Food:
    def __init__(self):
        self.position = [random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK),
                         random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)]
    
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, [self.position[0], self.position[1], SNAKE_BLOCK, SNAKE_BLOCK])
        
    def respawn(self):
        self.position = [random.randrange(0, WIDTH - SNAKE_BLOCK, SNAKE_BLOCK),
                         random.randrange(0, HEIGHT - SNAKE_BLOCK, SNAKE_BLOCK)]