import pygame

from config import paddle_width, paddle_height, paddle_speed, height, paddle_color

class Paddle:
  def __init__(self, x, y):
    self.rect = pygame.Rect(x, y, paddle_width, paddle_height)
    self.speed = paddle_speed


  def move(self, direction):
    self.rect.y -= direction * self.speed

    if self.rect.top < 0:
      self.rect.top = 0

    if self.rect.bottom > height:
      self.rect.bottom = height

  def draw(self, screen):
    pygame.draw.rect(screen, paddle_color, self.rect)