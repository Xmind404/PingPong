from config import height, width, running, tick_rate, background_color, paddle_width, game_points

from entities.ball import Ball
from entities.paddle import Paddle
from utils.draw_text import draw_text

import pygame
import random

def run_game():
  global running
  pygame.init()


  paddle1 = Paddle(0, height / 2)
  paddle2 = Paddle(width - paddle_width, height / 2)

  ball = Ball(width/2, height/2)
  ball_angle = random.choice([45.0, 135.0, -45.0, -135.0])

  temp_game_points: list[int] = [0, 0]


  screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
  clock = pygame.time.Clock()

  while running == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False



    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
      paddle1.move(1)

    if keys[pygame.K_s]:
      paddle1.move(-1)

    if keys[pygame.K_UP]:
      paddle2.move(1)

    if keys[pygame.K_DOWN]:
      paddle2.move(-1)

    screen.fill(background_color)

    if temp_game_points[0] < game_points[0] or temp_game_points[1] < game_points[1]:
      ball.x = width / 2
      ball.y = height / 2
      ball.rect.x = int(ball.x)
      ball.rect.y = int(ball.y)
      ball.visible = False
      ball_angle = random.choice([45.0, 135.0, -45.0, -135.0])

      paddle1.rect.y = height / 2
      paddle2.rect.y = height / 2

      paddle1.draw(screen)
      paddle2.draw(screen)
      ball.draw(screen)
      draw_text(f"{game_points[0]} | {game_points[1]}", pygame.font.SysFont("Arial", 100), (0, 0, 0), width // 2, height // 2, screen)
      pygame.display.flip()

      pygame.time.wait(1000)
      
      ball.visible = True

    else:
      draw_text(f"{game_points[0]} | {game_points[1]}", pygame.font.SysFont("Arial", 30), (0, 0, 0), width // 2, 20, screen)

    temp_game_points[0] = game_points[0]
    temp_game_points[1] = game_points[1]

    paddle1.draw(screen)
    paddle2.draw(screen)

    ball_angle = ball.move_by_radius(ball_angle, paddle1, paddle2)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(tick_rate)

  pygame.quit()
  return