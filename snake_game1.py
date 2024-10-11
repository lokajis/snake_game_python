import turtle
import time
import random
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
#Snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

#Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down" 
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
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
        #check for collision with the border 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() <-290:
        time.sleep(1)  
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        #body colision reset
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()            


    if head.distance(food) < 20:
        #moove the food to a random spot  
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
#MOve the segments end firstn in reverse order
    for i in range(len(segments)-1,0,-1):
        segments[i].goto(segments[i-1].xcor() , segments[i-1].ycor())
#move segment 0 to the hrad
    if len(segments) > 0 :
        segments[0].goto(head.xcor(), head.ycor())


    move()
    time.sleep(delay)


wn.mainloop()