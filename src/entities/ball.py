import pygame
import math
import random

from config import ball_width, ball_height, ball_speed, ball_color, width, height, ball_randomized_speed, game_points

class Ball:
  def __init__(self, x, y):
    self.x = float(x)
    self.y = float(y)
    self.rect = pygame.Rect(int(self.x), int(self.y), ball_width, ball_height)
    self.visible = True

    if ball_randomized_speed:
      min_speed = int(ball_speed - (0.5 * ball_speed))  
      max_speed = int(ball_speed + (0.5 * ball_speed))  
      self.speed = random.randint(min_speed, max_speed)
    else:
      self.speed = ball_speed



  def move_by_radius(self, angle_degrees: float, paddle1, paddle2, radius: float = None):
    distance = radius if radius is not None else self.speed

    angle_radians = math.radians(angle_degrees)

    move_x = distance * math.cos(angle_radians)
    move_y = distance * math.sin(angle_radians)

    self.x += move_x
    self.y += move_y
    
    self.rect.x = int(self.x)
    self.rect.y = int(self.y)


    if self.rect.x < 0:
      self.rect.x = 0
      self.x = 0.0
      angle_degrees = 180 - angle_degrees
      self.add_points(1)

      if ball_randomized_speed:
        min_speed = int(ball_speed - (0.5 * ball_speed))  
        max_speed = int(ball_speed + (0.5 * ball_speed))  
        self.speed = random.randint(min_speed, max_speed)
      else:
        self.speed = ball_speed

    elif self.rect.x > width - ball_width:
      self.rect.x = width - ball_width
      self.x = float(self.rect.x)
      angle_degrees = 180 - angle_degrees
      self.add_points(0)

      if ball_randomized_speed:
        min_speed = int(ball_speed - (0.5 * ball_speed))  
        max_speed = int(ball_speed + (0.5 * ball_speed))  
        self.speed = random.randint(min_speed, max_speed)
      else:
        self.speed = ball_speed



    else:
      if self.rect.colliderect(paddle1.rect):
        self.rect.left = paddle1.rect.right
        self.x = float(self.rect.x) 
        if ball_randomized_speed:
          min_speed = int(ball_speed - (0.5 * ball_speed))  
          max_speed = int(ball_speed + (0.5 * ball_speed))  
          self.speed = random.randint(min_speed, max_speed)
        else:
          self.speed = ball_speed

        angle_degrees = 180 - angle_degrees

      elif self.rect.colliderect(paddle2.rect):
        self.rect.right = paddle2.rect.left
        self.x = float(self.rect.x) 
        if ball_randomized_speed:
          min_speed = int(ball_speed - (0.5 * ball_speed))  
          max_speed = int(ball_speed + (0.5 * ball_speed))  
          self.speed = random.randint(min_speed, max_speed)
        else:
          self.speed = ball_speed

        angle_degrees = 180 - angle_degrees



    if self.rect.top < 0:
      self.rect.top = 0
      self.y = float(self.rect.y)
      angle_degrees = -angle_degrees
      if ball_randomized_speed:
        min_speed = int(ball_speed - (0.5 * ball_speed))  
        max_speed = int(ball_speed + (0.5 * ball_speed))  
        self.speed = random.randint(min_speed, max_speed)
      else:
        self.speed = ball_speed

    elif self.rect.bottom > height:
      self.rect.bottom = height
      self.y = float(self.rect.y)
      angle_degrees = -angle_degrees
      if ball_randomized_speed:
        min_speed = int(ball_speed - (0.5 * ball_speed))  
        max_speed = int(ball_speed + (0.5 * ball_speed))  
        self.speed = random.randint(min_speed, max_speed)
      else:
        self.speed = ball_speed   

    return angle_degrees



  def add_points(self, who):
    global game_points
    if who == 0:
      game_points[0] += 1
    if who == 1:
      game_points[1] += 1

  def draw(self, screen):
    if self.visible:
      pygame.draw.rect(screen, ball_color, self.rect)