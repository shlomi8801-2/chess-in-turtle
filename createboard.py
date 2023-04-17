<<<<<<< HEAD
import turtle
import math
screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0,0) #set turtle to istant move
squaresize = 50
unicodechess = ["wk","♔","bk","♚","wq","♕","bq","♛","wr","♖","br","♜","wb","♗","bb","♝","wn","♘","bn","♞","00"," ","wp","♙","bp","♟︎"]
board = ["00"]*64
global turn,selected
selected = "00"
piecesw = ["♖","♘","♗","♕","♔","♙","□","🗑"]
piecesb = ["♜","♞","♝","♛","♚","♟︎","■","🗑"]
turn = 0
file = open("board.txt","w") 
def findpiece(a):
    return unicodechess[unicodechess.index(a)+1]
def draw(squaresize,board0):
    t.clear()
    count = 0
    color = 0
    colors = ["#769656","#eeeed2"]
    for x in range(-1*squaresize*4,squaresize*4,squaresize):
        t.penup()
        for y in range(-1*squaresize*4,squaresize*4,squaresize):
            count = count+1
            t.goto(x,y)
            t.pendown()

            if color == 0:
                t.fillcolor(colors[1])
                color = 1
            else:
                t.fillcolor(colors[0])
                color = 0
            t.begin_fill()
            t.goto(x+squaresize,y)
            t.goto(x+squaresize,y+squaresize)
            t.goto(x,y+squaresize)
            t.goto(x,y)
            t.penup()
            t.pendown()
            t.write(findpiece(board0[count-1]),font=("Arial", squaresize-20, "normal"))
            t.end_fill()
            t.penup()
            t.goto(x,y)
        if color == 0:
            t.fillcolor("black")
            color = 1
        else:
            t.fillcolor("white")
            color = 0

    for y in range(-1*squaresize*4,squaresize*4,squaresize):
        
        t.goto(-5 * squaresize,y)
        if turn == 0:
            t.write(piecesw[y//squaresize+4],font=("Arial", squaresize-20, "normal"))
        elif turn == 1:
            t.write(piecesb[y//squaresize+4],font=("Arial", squaresize-20, "normal"))
    






    t.hideturtle()
draw(squaresize,board)

def click(x, y):
    
    global turn,selected
    clickedsquare = (int(x)//(squaresize)+4)*8+math.ceil(int(y)/squaresize)+3
    if 8+clickedsquare == 6:
        turn = abs(turn-1)
        print("changing color")
        draw(squaresize,board)

        return
    if 8+clickedsquare == 7:
        selected = "00"

        return
    if 8+clickedsquare <7:
        if turn == 0:
            selected = unicodechess.index(piecesw[8+clickedsquare])
        elif turn == 1:
            selected = unicodechess.index(piecesb[8+clickedsquare])

    else:
        if selected == "00":
            board[clickedsquare] = "00"
        else:
            board[clickedsquare] = unicodechess[selected-1]

    
    draw(squaresize,board)
    

turtle.onscreenclick(click)
screen.mainloop()
=======
import turtle
import math
screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0,0) #set turtle to istant move
squaresize = 50
unicodechess = ["wk","♔","bk","♚","wq","♕","bq","♛","wr","♖","br","♜","wb","♗","bb","♝","wn","♘","bn","♞","00"," ","wp","♙","bp","♟︎"]
board = ["00"]*64
global turn,selected
selected = "00"
piecesw = ["♖","♘","♗","♕","♔","♙","□","🗑"]
piecesb = ["♜","♞","♝","♛","♚","♟︎","■","🗑"]
turn = 0
file = open("board.txt","w") 
def findpiece(a):
    return unicodechess[unicodechess.index(a)+1]
def draw(squaresize,board0):
    t.clear()
    count = 0
    color = 0
    colors = ["#769656","#eeeed2"]
    for x in range(-1*squaresize*4,squaresize*4,squaresize):
        t.penup()
        for y in range(-1*squaresize*4,squaresize*4,squaresize):
            count = count+1
            t.goto(x,y)
            t.pendown()

            if color == 0:
                t.fillcolor(colors[1])
                color = 1
            else:
                t.fillcolor(colors[0])
                color = 0
            t.begin_fill()
            t.goto(x+squaresize,y)
            t.goto(x+squaresize,y+squaresize)
            t.goto(x,y+squaresize)
            t.goto(x,y)
            t.penup()
            t.pendown()
            t.write(findpiece(board0[count-1]),font=("Arial", squaresize-20, "normal"))
            t.end_fill()
            t.penup()
            t.goto(x,y)
        if color == 0:
            t.fillcolor("black")
            color = 1
        else:
            t.fillcolor("white")
            color = 0

    for y in range(-1*squaresize*4,squaresize*4,squaresize):
        
        t.goto(-5 * squaresize,y)
        if turn == 0:
            t.write(piecesw[y//squaresize+4],font=("Arial", squaresize-20, "normal"))
        elif turn == 1:
            t.write(piecesb[y//squaresize+4],font=("Arial", squaresize-20, "normal"))
    






    t.hideturtle()
draw(squaresize,board)

def click(x, y):
    
    global turn,selected
    clickedsquare = (int(x)//(squaresize)+4)*8+math.ceil(int(y)/squaresize)+3
    if 8+clickedsquare == 6:
        turn = abs(turn-1)
        print("changing color")
        draw(squaresize,board)

        return
    if 8+clickedsquare == 7:
        selected = "00"

        return
    if 8+clickedsquare <7:
        if turn == 0:
            selected = unicodechess.index(piecesw[8+clickedsquare])
        elif turn == 1:
            selected = unicodechess.index(piecesb[8+clickedsquare])

    else:
        if selected == "00":
            board[clickedsquare] = "00"
        else:
            board[clickedsquare] = unicodechess[selected-1]

    
    draw(squaresize,board)
    

turtle.onscreenclick(click)
screen.mainloop()
>>>>>>> 5bd9551 (upload files)
file.write("".join(board))