from config import height, width, running, tick_rate, background_color

import pygame as pygame

def run_game():
  global running
  pygame.init()
  
  screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
  clock = pygame.time.Clock()


  while running == True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False


    screen.fill(background_color)

    pygame.display.flip()

    clock.tick(tick_rate)

  pygame.quit()
  return