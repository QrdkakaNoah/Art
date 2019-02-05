import turtle, random
colors = ["red","green","blue","yellow"]

turtle = turtle.Turtle()
turtle.speed(0)
def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
square()
def art():
    for i in range(90):
        turtle.left(1)
        square()
art()
def passpartout():
    for i in range(4):
        art()
passpartout()
def passpartout2():
    for i in range(4):
        color = random.choice(colors)
        turtle.color(color)
        turtle.forward(200)
        art()
passpartout2()
def passpartout3():
    for i in range (4):
        color = random.choice(colors)
        turtle.color(color)
        turtle.left(180)
        turtle.forward(200)
        art()
passpartout3()

        

