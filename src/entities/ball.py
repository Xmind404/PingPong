import pygame
import math
import random

from config import ball_width, ball_height, ball_speed, ball_color, width, height, ball_randomized_speed

class Ball:
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)
    self.rect = pygame.Rect(int(self.x), int(self.y), ball_width, ball_height)
    
    if ball_randomized_speed:
      min_speed = int(ball_speed - (0.5 * ball_speed))  
      max_speed = int(ball_speed + (0.5 * ball_speed))  
      self.speed = random.randint(min_speed, max_speed)
    else:
      self.speed = ball_speed



  def move_by_radius(self, angle_degrees: float, radius: float = None):
    distance = radius if radius is not None else self.speed

    angle_radians = math.radians(angle_degrees)

    move_x = distance * math.cos(angle_radians)
    move_y = distance * math.sin(angle_radians)

    self.x += move_x
    self.y += move_y
    
    self.rect.x = int(self.x)
    self.rect.y = int(self.y)

    if self.rect.x <= 0 or self.rect.x >= width - ball_width:
      angle_degrees = 180 - angle_degrees
    if self.rect.y <= 0 or self.rect.y >= height - ball_height:
      angle_degrees = -angle_degrees

    return angle_degrees


  def draw(self, screen):
    pygame.draw.rect(screen, ball_color, self.rect)