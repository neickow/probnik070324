from turtle import *
tracer(50)
screensize(3000, 3000)
down()
left(90)
n=15
# шаблон выше
for i in range(23):
    forward(50*n)
    right(90)
up()
forward(10*n)
right(90)
forward(20*n)
down()
for i in range(34):
    forward(40*n)
    left(90)
# шаблон ниже
up()
color('red')
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*n, y*n)
        dot(3)
done()