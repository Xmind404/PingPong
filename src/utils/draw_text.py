def draw_text(text, font, text_col, x, y, screen):
  img = font.render(text, True, text_col)
  
  text_rect = img.get_rect()
  text_rect.center = (x, y)
  screen.blit(img, text_rect)