import math

from screeninfo import get_monitors


monitor = get_monitors()[0]
height = monitor.height
width = monitor.width

running = True
tick_rate = 60
game_speed = 1
background_color = "white"


ball_width = math.floor(width / 50)
ball_height = math.floor(width / 50)
ball_color = "black"

paddle_width = math.floor(width / 50)
paddle_height = math.floor(height / 10)
paddle_color = "black"
paddle_speed = 7