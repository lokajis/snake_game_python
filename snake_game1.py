import turtle
import time

delay = 0.1
# SETUP THE SCREEN

wn = turtle.Screen()
wn.title("Snake Game by Alexandros Economides")
wn.bgcolor("gray")
wn.setup(width=600, height=600)
# turns off animation from screen and also updates
wn.tracer(0)
#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("green")
#Turtle was to drow lines, now it doent draw anything
head.penup()
head.goto(0,0)
#it will be still at the midle when it starts
head.direction = "stop"
#Functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":  
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "right":  
       x = head.xcor()
       head.setx(x + 20)
    elif head.direction == "left":  
       x = head.xcor()
       head.setx(x - 20)  
#keybord binding
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)


wn.mainloop()