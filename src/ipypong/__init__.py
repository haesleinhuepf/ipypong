from ipycanvas import Canvas, hold_canvas
from IPython.display import display
import ipywidgets as widgets
import numpy as np
from ipywidgets import Output

__version__ = "0.1.0"


# Game variables
ball_x = 300
ball_y = 200
ball_speed_x = 5
ball_speed_y = 5
ball_radius = 10

paddle_left_y = 200
paddle_right_y = 200
paddle_width = 10
paddle_height = 60
paddle_speed = 10

score_left = 0
score_right = 0
canvas = None
num_players = 1  # Default to single player mode

def pong(players=1):
    global canvas, num_players
    num_players = players
    canvas = Canvas(width=600, height=400)
    out = Output()
    display(canvas)



    ### Game controls
    @out.capture()
    def handle_keydown(key, shift_key, ctrl_key, meta_key):
        global paddle_left_y, paddle_right_y

        # Only handle keyboard input if not in 0-player mode
        if num_players > 0:
            # Left paddle controls (Player 1)
            if key == 'w' and paddle_left_y > 0:
                paddle_left_y -= paddle_speed
            elif key == 's' and paddle_left_y < canvas.height - paddle_height:
                paddle_left_y += paddle_speed
            
            # Right paddle controls (Player 2)
            if num_players == 2:
                if key == 'i' and paddle_right_y > 0:
                    paddle_right_y -= paddle_speed
                elif key == 'k' and paddle_right_y < canvas.height - paddle_height:
                    paddle_right_y += paddle_speed

    canvas.on_key_down(handle_keydown)



    timer = widgets.Play(interval=16, max=10000000)
    widgets.jslink((timer, 'value'), (widgets.IntText(), 'value'))
    timer.observe(game_loop, 'value')
    #timer.on_key_down(handle_keydown)  # Add key handler to timer as well

    display(timer)
    timer.playing = True


def game_loop(change):
    global canvas, ball_x, ball_y, ball_speed_x, ball_speed_y, score_left, score_right, paddle_right_y, paddle_left_y

    # AI player movement
    if num_players < 2:  # Right paddle AI (for 0 or 1 player mode)
        if ball_y > paddle_right_y + paddle_height/2:
            paddle_right_y = min(paddle_right_y + paddle_speed, canvas.height - paddle_height)
        elif ball_y < paddle_right_y + paddle_height/2:
            paddle_right_y = max(paddle_right_y - paddle_speed, 0)
            
    if num_players == 0:  # Left paddle AI (for 0 player mode)
        if ball_y > paddle_left_y + paddle_height/2:
            paddle_left_y = min(paddle_left_y + paddle_speed, canvas.height - paddle_height)
        elif ball_y < paddle_left_y + paddle_height/2:
            paddle_left_y = max(paddle_left_y - paddle_speed, 0)

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collisions with walls
    if ball_y <= 0 or ball_y >= canvas.height:
        ball_speed_y *= -1

    # Ball collisions with paddles
    if (ball_x - ball_radius <= paddle_width and
        paddle_left_y <= ball_y <= paddle_left_y + paddle_height):
        ball_speed_x *= -1
        ball_x = paddle_width + ball_radius

    if (ball_x + ball_radius >= canvas.width - paddle_width and
        paddle_right_y <= ball_y <= paddle_right_y + paddle_height):
        ball_speed_x *= -1
        ball_x = canvas.width - paddle_width - ball_radius

    # Score points
    if ball_x <= 0:
        score_right += 1
        ball_x = canvas.width / 2
        ball_y = canvas.height / 2
    elif ball_x >= canvas.width:
        score_left += 1
        ball_x = canvas.width / 2
        ball_y = canvas.height / 2

    # Draw everything
    with hold_canvas(canvas):
        canvas.clear()
        canvas.fill_style = 'white'
        canvas.fill_rect(0, 0, canvas.width, canvas.height)
        canvas.fill_style = 'black'
        canvas.fill_rect(0, paddle_left_y, paddle_width, paddle_height)
        canvas.fill_rect(canvas.width - paddle_width, paddle_right_y,
                        paddle_width, paddle_height)
        canvas.fill_circle(ball_x, ball_y, ball_radius)
        canvas.font = '30px Arial'
        canvas.fill_text(str(score_left), canvas.width/4, 50)
        canvas.fill_text(str(score_right), 3*canvas.width/4, 50)
        canvas.focus()
