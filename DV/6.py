from turtle import *

tracer(0)
m = 30

for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)
up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()
for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)
up()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(5, "red")
update()
input()