from config import height, width, running, tick_rate, background_color, paddle_width

from entities.ball import Ball
from entities.paddle import Paddle


import pygame as pygame

def run_game():
  global running
  pygame.init()


  paddle1 = Paddle(0, height / 2)
  paddle2 = Paddle(width - paddle_width, height / 2)
  
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
    paddle1.draw(screen)
    paddle2.draw(screen)


    pygame.display.flip()
    clock.tick(tick_rate)

  pygame.quit()
  return