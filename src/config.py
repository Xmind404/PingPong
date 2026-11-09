from screeninfo import get_monitors

monitor = get_monitors()[0]
height = monitor.height
width = monitor.width

running = True
tick_rate = 60
game_speed = 1

background_color = "white"
ball_color = "black"
paddle_color = "black"