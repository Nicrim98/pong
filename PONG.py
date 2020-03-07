import turtle
import time
import os
import sys
import subprocess

# pełna kompatybilność na systemie MacOS, na Windowsie próbowałem odpalić, wszystko działa z tym że
# prędkości początkowe są za szybkie, info nie jest poprawnie sformatowane i tym podobne

info_file = "info.txt"

global winner_txt
window = turtle.Screen()
window.title("PONG")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Stan poczatkowy punktow
score_a = 0
score_b = 0
ending_score = 3
ball_speed = 2

# Paddle A
paddle_a = turtle.Turtle()  # inicjalizacja lewego panelu
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()  # brak pozostawiania sladu po ruchu
paddle_a.goto(-350, 0)  # poczatkowa pozycja

# Paddle B
paddle_b = turtle.Turtle()  # inicjalizacja prawego panelu
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()  # brak pozostawiania sladu po ruchu
paddle_b.goto(350, 0)  # poczatkowa pozycja

# Ball
ball = turtle.Turtle()  # inicjalizacja pilki
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()  # brak pozostawiania sladu po ruchu
ball.goto(0, 0)  # poczatkowa pozycja
ball.dx = 0
ball.dy = 0

# Punktowanie
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# wypisanie zwyciezcy
winner_txt = turtle.Turtle()
winner_txt.speed(0)
winner_txt.color("white")
winner_txt.penup()
winner_txt.hideturtle()
winner_txt.goto(0, 0)

# Zagraj/koniec gry
menu = turtle.Turtle()
menu.speed(0)
menu.color("white")
menu.penup()
menu.hideturtle()

#  wyswietlenie ekranu poczatkowego
def menu_show():
    menu.goto(0, 100)
    menu.write("Start - press o", align="center", font=("Courier", 24, "normal"))
    menu.goto(0, 80)
    menu.write("Quit - press k", align="center", font=("Courier", 24, "normal"))
    menu.goto(0, -260)
    menu.write("Info - press i", align="center", font=("Courier", 24, "normal"))
menu_show()

# otworzenie pliku z infem
def info():
    if sys.platform == "win32":
        os.startfile(info_file)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, info_file])


# Functions for moving objects
def paddle_a_up():
    y = paddle_a.ycor()  # ycor() zwraca wspolrzedna y
    y += 20
    paddle_a.sety(y)
    if ball.dx > 4:     # zwiekszenie szybkosci panelu jesli jest wieksza predkosc pilki
        y = paddle_a.ycor()
        y += 30
        paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()  # ycor() zwraca wspolrzedna y
    y -= 20
    paddle_a.sety(y)
    if ball.dx > 4:     # zwiekszenie szybkosci panelu jesli jest wieksza predkosc pilki
        y = paddle_a.ycor()
        y -= 30
        paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()  # ycor() zwraca wspolrzedna y
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()  # ycor() zwraca wspolrzedna y
    y -= 20
    paddle_b.sety(y)

# ruch myszka
def dragging(x, y):
    x = 350
    paddle_b.ondrag(None)
    paddle_b.setheading(paddle_b.towards(x, y))
    paddle_b._rotate(90)
    paddle_b.sety(y)
    paddle_b.ondrag(dragging)

# start gry - puszczenie pilki
def play():
    global pen, winner_txt
    time.sleep(0.5)
    pen.clear()
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
    menu.clear()
    winner_txt.clear()
    ball.showturtle()
    ball.goto(0, 0)
    ball.dx = ball_speed
    ball.dy = ball_speed

# odpowiednie zwiekszanie predkosci pilki
def more_speed_1():
    if ball.dx < 0:
        ball.dx = -1
    else:
        ball.dx = 1


def more_speed_2():
    if ball.dx < 0:
        ball.dx = -2
    else:
        ball.dx = 2


def more_speed_3():
    if ball.dx < 0:
        ball.dx = -3
    else:
        ball.dx = 3


def more_speed_4():
    if ball.dx < 0:
        ball.dx = -4
    else:
        ball.dx = 4


def more_speed_5():
    if ball.dx < 0:
        ball.dx = -5
    else:
        ball.dx = 5


def more_speed_6():
    if ball.dx < 0:
        ball.dx = -6
    else:
        ball.dx = 6


def more_speed_7():
    if ball.dx < 0:
        ball.dx = -7
    else:
        ball.dx = 7


def more_speed_8():
    if ball.dx < 0:
        ball.dx = -8
    else:
        ball.dx = 8

def more_speed_9():
    if ball.dx < 0:
        ball.dx = -9
    else:
        ball.dx = 9

# zatrzymanie gry
def pause():
     global temp_dx, temp_dy
     temp_dx = ball.dx
     temp_dy = ball.dy
     ball.dx = 0
     ball.dy = 0

#wznowienie gry po wczesniejszej pause()
def resume():
    ball.dx = temp_dx
    ball.dy = temp_dy

# zakonczenie gry
def leave():
    turtle.Screen().bye()


# Powiazanie gry z przyciskami
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
paddle_b.ondrag(dragging)
window.onkeypress(more_speed_1, "1")
window.onkeypress(more_speed_2, "2")
window.onkeypress(more_speed_3, "3")
window.onkeypress(more_speed_4, "4")
window.onkeypress(more_speed_5, "5")
window.onkeypress(more_speed_6, "6")
window.onkeypress(more_speed_7, "7")
window.onkeypress(more_speed_8, "8")
window.onkeypress(more_speed_9, "9")
window.onkeypress(play, "o")
window.onkeypress(leave, "k")
window.onkeypress(pause, "p")
window.onkeypress(resume, "r")
window.onkeypress(info, "i")

# Glowna petla gry
while True:

    window.update()

    # ruch pilki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # zablokowanie scian dla pilki
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # zmienienie kierunku ruchu pilki w plaszczyznie

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # zmienienie kierunku ruchu pilki w plaszczyznie y

    # zablokowanie scian dla paneli
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # uderzenie pilki w panel
    if ball.xcor() > 390:   # case uderzenie poza panel b
        ball.goto(0, 0)  # wtedy pilka wraca do pozycji startowej, punkt dla panelu a,
        ball.dx = ball_speed
        ball.dy = ball_speed
        pause()         # chwilowe wstrzymanie gry żeby piłka nie za szybko wystartowała
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.5)
        resume()

    if ball.xcor() < -390:
        ball.goto(0, 0) # case uderzenie poza panel a
        ball.dx = -ball_speed  # wtedy pilka wraca do pozycji startowej, punkt dla panelu b, chwilowe wstrzymanie gry
        ball.dy = -ball_speed
        pause()         # chwilowe wstrzymanie gry żeby piłka nie za szybko wystartowała
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        time.sleep(0.5)
        resume()

    # zderzenie z panelem, pilka sie odbija
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50) and (ball.ycor() > paddle_b.ycor() - 50):
        ball._rotate(90)
        ball.dx *= -1

    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50) and (ball.ycor() > paddle_a.ycor() - 50):
        ball._rotate(90)
        ball.dx *= -1

    # zakonczenie gry - dwa casy
    if score_b == ending_score:
        ball.hideturtle()
        time.sleep(0.5)
        winner_txt.write("Player B has won !", align="center", font=("Ariel", 36, "bold"))
        menu_show()
        score_b = 0
        score_a = 0

    if score_a == ending_score:
        ball.hideturtle()
        time.sleep(0.5)
        winner_txt.write("Player A has won !", align="center", font=("Ariel", 36, "bold"))
        menu_show()
        score_a = 0
        score_b = 0
