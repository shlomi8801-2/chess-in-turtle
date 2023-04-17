import turtle
screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0,0) #set turtle to istant move
squaresize = 50
screen.screensize(squaresize*8,squaresize*8)

def draw():
    for x in range(-1*squaresize*4,squaresize*4+1,squaresize):
        t.penup()
        for y in range(-1*squaresize*4,squaresize*4,squaresize):
            t.goto(x,y)
            t.pendown()
            t.goto(x+squaresize,y)
            t.goto(x+squaresize,y+squaresize)
            t.goto(x,y+squaresize)
            t.goto(x,y)
            t.penup()
            t.pendown()
            t.write("♜",font=("Arial", squaresize-20, "normal"))
            t.penup()
            t.goto(x,y)
    t.hideturtle()
draw()



screen.exitonclick()