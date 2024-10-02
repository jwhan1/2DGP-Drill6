from pico2d import *
import random
import math
width = 800
height = 600

open_canvas()


hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

def move_character():
    global x, y, t
    if (x == handX and y == handY):
        move_hand()
    if abs(x - handX) < 2:
        t = 0
    else:
        t =  1 - t / (math.sqrt(width ** 2 + height ** 2))**(2/3)

    x = (1- t) * handX + t * x
    y = (1- t) * handY + t * y

def move_hand():
    global handX, handY

    handX = random.randrange(25, width - 25)
    handY = random.randrange(26, height - 26)

    move = 0
running = True

x = width // 2.0
y = height // 2.0
t = 0.1;
handX = x
handY = y
frame = 0
while running:
    clear_canvas()
    background.draw(width // 2, height // 2)
    move_character()# 이동
    # 그리기
    hand_arrow.draw(handX, handY)
    character.clip_draw(frame * 100, 100, 100, 100, x, y, 100, 100)
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.001)


close_canvas()