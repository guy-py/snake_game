from tkinter import*
from time import sleep
from random import randint
from random import choice
window = Tk()
window.title('snake.py')
c = Canvas(window, height=650, width=1000, bg='black')
c.pack()
title = c.create_text(500, 70, text='SNAKE', font=('', 70), fill='white')
score = c.create_text(25,25, text='0', font=('', 40), fill='white')
Quit = c.create_rectangle(400, 360, 600, 440, fill='white')
play = c.create_rectangle(400, 180, 600, 260, fill='white')
tuit = c.create_text(500, 400, text='[Q]QUIT', font=('', 40), fill='black')
tlay = c.create_text(500, 220, text='[L]PLAY', font=('', 40), fill='black')
sett = c.create_rectangle(360, 540, 640, 620, fill='white')
tett = c.create_text(500, 580, text='[S]SETTINGS', font=('', 40), fill='black')
class snake:
    direction = "Right"
    boxes = []
    inter = 'menu'
    a = []
    eat = True
    score = 0
    sleep = 0.3
    col = ['lime', 'white', 'pink', 'blue']
    a_col = 'red'
col1 = c.create_rectangle(400, 450, 500, 350, fill=snake.col[0], state=HIDDEN)
def set_menu():
    c.itemconfig(title, state=NORMAL)
    c.itemconfig(title, text='SNAKE')
    c.itemconfig(score, state=HIDDEN)
    c.itemconfig(Quit, state=NORMAL)
    c.itemconfig(play, state=NORMAL)
    c.itemconfig(tuit, state=NORMAL)
    c.itemconfig(tlay, state=NORMAL)
    c.itemconfig(sett, state=NORMAL)
    c.itemconfig(tett, state=NORMAL)
    c.itemconfig(tlay, text='[L]PLAY')
    c.itemconfig(tuit, text='[Q]QUIT')
    for i in snake.boxes:
        c.delete(i)
    snake.boxes = []
    for i in snake.a:
        c.delete(i)
    snake.a = []
def set_play():
    if True:
        c.itemconfig(title, state=HIDDEN)
        c.itemconfig(score, state=NORMAL)
        c.itemconfig(Quit, state=HIDDEN)
        c.itemconfig(play, state=HIDDEN)
        c.itemconfig(tuit, state=HIDDEN)
        c.itemconfig(tlay, state=HIDDEN)
        c.itemconfig(sett, state=HIDDEN)
        c.itemconfig(tett, state=HIDDEN)
        if snake.eat:
            apple(randint(0, 19), randint(0, 12))
            snake.eat = False
            snake.boxes.append(c.create_rectangle(-50, -50, 0, 0, fill=choice(snake.col)))
        prev = get(snake.boxes[0])
        if snake.direction == "Down":
            c.move(snake.boxes[0], 0, 50)
        elif snake.direction == "Up":
            c.move(snake.boxes[0], 0, -50)
        elif snake.direction == "Right":
            c.move(snake.boxes[0], 50, 0)
        elif snake.direction == "Left":
            c.move(snake.boxes[0], -50, 0)
        if ((get(snake.boxes[0])[1] >= 650 and snake.direction == "Down") or (get(snake.boxes[0])[1] <= -50 and snake.direction == "Up")) or ((get(snake.boxes[0])[0] <= -50 and snake.direction == "Left") or (get(snake.boxes[0])[0] >= 1000 and snake.direction == "Right")):
            snake.inter = 'lose'
        how = 1
        for i in snake.boxes:
            if not how == 1:
                if True:
                    trev = get(i)
                    go_to(i, prev[0], prev[1])
                    prev = trev
            how = how + 1
        for j in snake.a:
            for i in snake.boxes:
                if len(c.coords(j)) == 4:
                    if get(i) == get(j):
                        snake.boxes.append(c.create_rectangle(-50, -50, 0, 0))
                        snake.eat = True
                        c.delete(j)
                        del snake.boxes[ffind(snake.boxes, j) - 1]
                        snake.score += 1
                        snake.sleep = snake.sleep - 0.008
        for i in snake.boxes:
            for j in snake.boxes:
                if get(i) == get(j) and not i == j:
                    snake.inter = 'lose'
        c.itemconfig(score, text=snake.score)
        sleep(snake.sleep)
def set_lose():
    if True:
        c.itemconfig(title, state=NORMAL)
        c.itemconfig(title, text='GAME OVER')
        c.itemconfig(score, state=NORMAL)
        c.itemconfig(Quit, state=NORMAL)
        c.itemconfig(play, state=HIDDEN)
        c.itemconfig(tuit, state=NORMAL)
        c.itemconfig(tlay, state=HIDDEN)
        c.itemconfig(tuit, text='[M]MENU')
    c.itemconfig(sett, state=HIDDEN)
    c.itemconfig(tett, state=HIDDEN)
def set_pause():
    if True:
        c.itemconfig(title, state=NORMAL)
        c.itemconfig(title, text='PAUSED')
        c.itemconfig(score, state=NORMAL)
        c.itemconfig(Quit, state=NORMAL)
        c.itemconfig(play, state=NORMAL)
        c.itemconfig(tuit, state=NORMAL)
        c.itemconfig(tlay, state=NORMAL)
        c.itemconfig(tlay, text='[L]PLAY')
        c.itemconfig(tuit, text='[M]MENU')
    c.itemconfig(sett, state=HIDDEN)
    c.itemconfig(tett, state=HIDDEN)
def ffind(l, o):
    count = 0
    for i in l:
        if i == o:
            re = count
            break
        count += 1
    return count
def snake_setup():
    for i in snake.boxes:
        c.delete(i)
    snake.boxes = []
    snake.boxes = [c.create_rectangle(50, 50, 100, 100, fill=choice(snake.col)), c.create_rectangle(-50, -50, 0, 0, fill=choice(snake.col))]
    snake.score = 0
    snake.direction = "Down"
    snake.eat = True
    snake.sleep = 0.3
def apple(x, y):
    x=x*50
    y=y*50
    snake.a.append(c.create_rectangle(x, y, x+50, y+50, fill='red'))
def key(e):
    if snake.inter == 'playing':
        e = e.keysym
        if e == "Down" or e == "Up" or e == "Left" or e == "Right":
            if (not e == "Down" and snake.direction == "Up") or (not e == "Left" and snake.direction == "Right") or (not e == "Up" and snake.direction == "Down") or (not e == "Right" and snake.direction == "Left"):
                snake.direction = e
        if e == "p":
            snake.inter = 'pause'
    elif snake.inter == 'menu':
        e = e.char
        if e == 'l':
            snake.inter = 'playing'
            snake_setup()
        elif e == 'q':
            quit()
    elif snake.inter == 'lose':
        e = e.char
        if e == 'm':
            snake.inter = 'menu'
    elif snake.inter == 'pause':
        e = e.char
        if e == 'l':
            snake.inter = 'playing'
        if e == 'm':
            snake.inter = 'menu'
c.bind_all('<Key>', key)
def get(iD):
    return [c.coords(iD)[0], c.coords(iD)[1]]
def go_to(iD, x, y):
    c.move(iD, x - get(iD)[0], y - get(iD)[1])
while True:
    c.update()
    if snake.inter == 'playing':
        set_play()
    elif snake.inter == 'lose':
        set_lose()
    elif snake.inter == 'menu':
        set_menu()
    elif snake.inter == 'pause':
        set_pause()
