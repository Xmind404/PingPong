import pygame

from config import ball_width, ball_height

class Ball:
  def __init__(self, x, y):
    self.rect = pygame.Rect(x, y)