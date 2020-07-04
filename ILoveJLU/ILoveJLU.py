# coding: UTF-8

# The code is in a mess.It is just a souvenir.

import turtle

t=turtle.Pen()
t.pensize(5)
t.speed(2)

def goto_by_list(location_list):
	for location in location_list:
		t.goto(location[0],location[1])

# 'I'
t.penup()
t.goto(-200-100,160)
t.pendown()
location_list = (
    (-200-30,160),
    (-200-65,160),
    (-200-65,0),
    (-200-100,0),
    (-200-30,0)
)
goto_by_list(location_list)

# 'Love'
t.pencolor("red")
t.penup()
t.goto(-200+100,0)
t.pendown()
t.left(45)
t.fd(100)

t.speed(6)
t.circle(50,180)
t.speed(2)

t.right(90)

t.speed(6)
t.circle(50,180)
t.speed(2)

t.fd(100)

t.speed(2)
t.left(45)

# 'JLU'
t.pencolor("black")
t.penup()
t.goto(-200+280,160)
t.pendown()
t.goto(-200+280,50)
t.left(90)

t.speed(6)
t.circle(50,-180)
t.speed(2)

t.penup()
t.goto(-200+300,160)
t.pendown()
t.goto(-200+300,0)
t.goto(-200+370,0)

t.penup()
t.goto(-200+390,160)
t.pendown()
t.goto(-200+390,50)

t.speed(6)
t.circle(50,180)
t.speed(2)

t.fd(110)

t.penup()
input()