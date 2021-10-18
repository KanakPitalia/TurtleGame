#importing required modules

import random
import turtle
score = 0
#adding screen
windo = turtle.Screen()
windo.setup(width=1.0,height=1.0)
windo.bgcolor('dark blue')

#adding player i.e turtle
player = turtle.Turtle()
player.color('light blue')
player.shape('turtle')

#drawing boundary line

player.hideturtle()
player.pu()
player.setposition(-300, 300)
player.pd()
player.speed(0)
for i in range(0, 4):
    player.forward(600)
    player.right(90)

player.showturtle()
player.pu()
player.setpos(0, 0)

player.speed(6)

#adding movement buttons and criteria

def k1():
    player.forward(5)
    player.speed(1)


def k2():
    player.left(20)


def k3():
    player.right(20)


def k4():
    player.back(5)

#function to quit game screen with any key other than up down right left
    
def k5():
    print("Your Score is",score)
    windo.bye()


windo.onkey(k1, 'Up')
windo.onkey(k2, 'Left')
windo.onkey(k3, 'Right')
windo.onkey(k4, 'Down')
windo.onkey(k5, '')
windo.listen()

#adding food

a = []
for i in range(6):
    obj = turtle.Turtle()
    obj.color('red')
    obj.shape('circle')
    obj.pu()
    obj.ht()
    obj.setpos(random.randrange(-285, 285), random.randrange(-285, 285))
    obj.st()
    a.append(obj)

player.speed(1)
windo.tracer(0)
t = turtle.Turtle()
t.ht()
t.pu()
t.setpos(0, 310)
t.pd()

#adding scroreboard


t.color("white")
t.write('Score={}'.format(score), align="center",
        font=("courier", 24, 'normal'))

#adding restrictions for turtle and food to never cross boundary line
#and random pop of food when eaten

while True:
    windo.update()
    if player.xcor() >= 280 or player.xcor() <= -280:
        player.left(180)
    elif player.ycor() >= 280 or player.ycor() <= -280:
        player.left(180)

    player.forward(0.5)

    for i in range(6):
        # a[i].st()
        a[i].speed(1)
        a[i].fd(0.07)

        if a[i].xcor() >= 280 or a[i].xcor() <= -280:
            a[i].left(180)
            a[i].setheading(random.randrange(360))

        elif a[i].ycor() >= 280 or a[i].ycor() <= -280:
            a[i].left(180)
            a[i].setheading(random.randrange(360))

        if player.distance(a[i]) <= 20:
            # player.turtlesize(int(i))
            a[i].speed(int(i)+1)
            a[i].ht()
            a[i].setpos(random.randrange(-285, 285),
                        random.randrange(-285, 285))
            a[i].st()
            score = score+2
            t.clear()
            t.color("white")
            t.write('Score={}'.format(score),
                    align="center", font=("courier", 24))

#to hold screen
windo.mainloop()
