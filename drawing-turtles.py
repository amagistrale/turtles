import turtle

t = turtle.Turtle()
t.pencolor('green')
t.pensize(10)
t.speed(1000)
t.left(90)
t.forward(250)

def petal():
    count=0
    while count <100:
        t.forward(1)
        t.right(0.5)
        count=count+1
    t.right(130)
    count=0
    while count <100:
         t.forward(1)
         t.right(0.5)
         count=count+1

t.pencolor('light blue')
t.pensize(10)
count=0
while count < 11:
    petal()
    count=count+1

t.pencolor('yellow')
t.pensize(15)
count=0
while count<10:
    t.forward(2)
    t.right(40)
    count=count+1
input('hit enter to exit')
