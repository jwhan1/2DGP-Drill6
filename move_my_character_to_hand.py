from pico2d import *
import random
width = 800
height = 600

open_canvas()


hand_arrow = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')
background = load_image('TUK_GROUND.png')

def move_character():

    pass

def draw_character():
    character.clip_draw(frame*100,100,100,100,x,y,100,100)
    pass

running = True
move = False
x = width // 2
y = height // 2
handX = random.randrange(25, width - 25)
handY = random.randrange(26, height - 26)
frame = 0
while running:
    clear_canvas()
    background.draw(width // 2, height // 2)
    move_character()#캐릭터 이동
    draw_character()#캐릭터 그리기
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.05)


close_canvas()