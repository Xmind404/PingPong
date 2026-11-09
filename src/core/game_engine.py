from config import height, width, running, tick_rate, background_color, paddle_width, game_points

from entities.ball import Ball
from entities.paddle import Paddle
from utils.draw_text import draw_text

import pygame

def run_game():
  global running
  pygame.init()


  paddle1 = Paddle(0, height / 2)
  paddle2 = Paddle(width - paddle_width, height / 2)
  ball = Ball(width/2, height/2)
  ball_angle = 45.0

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
    draw_text(f"{game_points[0]} | {game_points[1]}", pygame.font.SysFont("Arial", 30), (0, 0, 0), width // 2, 0, screen)

    paddle1.draw(screen)
    paddle2.draw(screen)

    ball_angle = ball.move_by_radius(ball_angle)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(tick_rate)

  pygame.quit()
  return