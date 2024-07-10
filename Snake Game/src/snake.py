import pygame
from src.settings import GREEN, SNAKE_BLOCK

class Snake:
    def __init__(self):
        self.length = 1
        self.segments = [[300, 200]]
        
    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_BLOCK, SNAKE_BLOCK])
    
    def move(self, direction):
        head = self.segments[-1][:]
        if direction == 'UP':
            head[1] -= SNAKE_BLOCK
        elif direction == 'DOWN':
            head[1] += SNAKE_BLOCK
        elif direction == 'LEFT':
            head[0] -= SNAKE_BLOCK
        elif direction == 'RIGHT':
            head[0] += SNAKE_BLOCK
            
        self.segments.append(head)
        if len(self.segments) > self.length:
            del self.segments[0]