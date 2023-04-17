import math
import turtle
abc = [*"abcdefgh"]
unicodechess = ["wk","♔","bk","♚","wq","♕","bq","♛","wr","♖","br","♜","wb","♗","bb","♝","wn","♘","bn","♞","00"," ","wp","♙","bp","♟︎"]
normalboard = "wrwp00000000bpbrwnwp00000000bpbnwbwp00000000bpbbwqwp00000000bpbqwkwp00000000bpbkwbwp00000000bpbbwnwp00000000bpbnwrwp00000000bpbr"
try: open("board.txt")
except: open("board.txt", "w").write(normalboard)
# normalboard = open("board.txt", "r").read()




class game:
    turn = 0








screen = turtle.Screen()
t = turtle.Turtle()
turtle.tracer(0,0) #set turtle to istant move
squaresize = 50
t.hideturtle()
moveable = []

#create board
def cb(e):
    board = []
    for x in range(len(abc)):
        for y in range(1,9,1):
            if e:
                board.append(abc[x]+str(y))
            else:
                board.append([normalboard[i:i+2] for i in range(0, len(normalboard), 2)][len(abc)*x+y-1])
    return board
# def findin(b,c):
board0 = cb(False)
def findpiece(a):
    return unicodechess[unicodechess.index(a)+1]
def draw(squaresize):
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
            t.goto(x,y)
            t.write(findpiece(board0[count-1]),font=("Arial", squaresize-20, "normal"))
            t.end_fill()
            t.goto(x,y)
            t.penup()
            t.goto(x,y)
        if color == 0:
            t.fillcolor("black")
            color = 1
        else:
            t.fillcolor("white")
            color = 0
    t.hideturtle()
def main():
    #setup screen
    screen.setup(squaresize*9,squaresize*9)
    screen.title("Sess - the better chess")
    draw(squaresize)
def blocktocord(b):
    out= 0
    out = out + (abc.index(b[0])+1)*8 + int((b[1]))+1
    return out
def drawcircle(block):
    t.penup()
    x = (block)//8 * squaresize -4*squaresize +squaresize/4
    y = (block)%8 * squaresize - 4*squaresize - squaresize/4
    t.goto(x,y)
    t.pendown()
    t.write("⊕",font=("Arial", squaresize, "normal"))
    t.penup()
def redraw(circles):
    t.clear()
    draw(squaresize)
    for i in circles:
        drawcircle(i)
def checkmove(block):
    moveable = []
    peice = board0[block]
    clickedpieces = block
    #pawn movment
    if block == -1:
        return []
    if peice == "00":
        return []
    if peice[1] == "p":
        if peice[0] == "w":
            if board0[block+1] == "00" and block+1 <= 63:
                # print("pawncan go")
                t.clear()
                moveable.append(block+1)
                if board0[block+2] == "00" and block+2 <= 63 and block % 8 == 1:
                    moveable.append(block+2)
        elif peice[0] == "b":
            if board0[block-1] == "00" and block-1 >= 0:
                # print("pawncan go")
                t.clear()
                moveable.append(block-1)
                if board0[block-2] == "00" and block-2 >= 0 and block % 8 == 6:
                    moveable.append(block-2)
    # rook movement
    if peice[1] == "r":
        # vertical movement UWU
        # check move down
        for x in range(block-1,block-block%8-1,-1):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
        # check move up
        for x in range(block+1,block-block%8+8,1):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:    
                break
        # horizontal movement
        # check move right
        for x in range(block+8,57+block%8,8):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
        # check move left
        for x in range(block-8,block%8-1,-8):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
    # horsy movement
    if peice[1] == "n":
        possiblemoves = [-17,-15,-10,-6,6,10,15,17]
        for x in possiblemoves:
            if block + x >= 0 and block +x <= 64 and abs((block+x) % 8 - block % 8) <= 2 and board0[block+x][0] != board0[block][0]:
                moveable.append(block+x)
    # bishop movement
    if peice[1] == "b":
        # up right check problem with top corner
        if block+9<=63:
            for x in range(block+9,64,9):
                print(x%8 , block%8)
                if board0[x] == "00" and x%8 > block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 > block%8:
                    moveable.append(x)
                    break
                else:     
                    break
            # up left

        if block-7>=0:
            for x in range(block-7,0,-7):
                if board0[x] == "00" and x%8 > block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 > block%8:
                    moveable.append(x)
                    break
                else:   
                    break   
        if block-8>=0:
            #  x%8 < block%8 for down checking
            # down right check 
            for x in range(block+7,64,+7):
                if board0[x] == "00" and x%8 < block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 < block%8:
                    moveable.append(x)
                    break
                else:
                    
                    break
            # down left
        if block-9>=0:
            for x in range(block-9,-1,-9):
                if board0[x] == "00" and x%8 < block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 < block%8:
                    moveable.append(x)
                    break
                else:     
                    break
    # queen movement
    if peice[1] == "q":
                # up right check
        if block+9<=63:
            for x in range(block+9,64,9):
                print(x%8 , block%8)
                if board0[x] == "00" and x%8 > block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 > block%8:
                    moveable.append(x)
                    break
                else:     
                    break
            # up left

        if block-7>=0:
            for x in range(block-7,0,-7):
                if board0[x] == "00" and x%8 > block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 > block%8:
                    moveable.append(x)
                    break
                else:   
                    break   
        if block-8>=0:
            #  x%8 < block%8 for down checking
            # down right check 
            for x in range(block+7,64,+7):
                if board0[x] == "00" and x%8 < block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 < block%8:
                    moveable.append(x)
                    break
                else:
                    
                    break
            # down left
        if block-9>=0:
            for x in range(block-9,-1,-9):
                if board0[x] == "00" and x%8 < block%8:
                    moveable.append(x)
                elif board0[block][0] != board0[x][0] and x%8 < block%8:
                    moveable.append(x)
                    break
                else:     
                    break
        # vertical movement UWU
        # check move down
        for x in range(block-1,block-block%8-1,-1):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
        # check move up
        for x in range(block+1,block-block%8+8,1):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:    
                break
        # horizontal movement
        # check move right
        for x in range(block+8,57+block%8,8):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
        # check move left
        for x in range(block-8,block%8-1,-8):
            if board0[x] == "00":
                moveable.append(x)
            elif board0[block][0] != board0[x][0]:
                moveable.append(x)
                break
            else:
                break
    if peice[1] == "k":
        possiblemoves = [-9,-8,-7,-1,1,7,8,9]
        for x in possiblemoves:
            if block + x >= 0 and block +x <= 64 and abs((block+x) % 8 - block % 8) <= 2 and board0[block+x][0] != board0[block][0]:
                moveable.append(block+x)
        
    # finnaly remake the whole screen with the circles

    print(moveable)
    return moveable
clicked = False
def changeturn(a):
    if a == True:
        game.turn = abs(game.turn - 1)
    return game.turn
def click(x, y):
    global moveable, checkpiece, clicked
    #turn = 0 means white turn
    clickedsquare = (int(x)//(squaresize)+4)*8+math.ceil(int(y)/squaresize)+3
    clickedsquarecord = abc[(int(x)//(squaresize)+4)]+str(math.ceil(int(y)/squaresize)+4)
    if (board0[clickedsquare][0] == "b" and changeturn(False) == 1) or (board0[clickedsquare][0] == "w" and changeturn(False) == 0):
        ml = checkmove(clickedsquare)
        if len(ml) != 0:
            checkpiece = clickedsquare
            if (changeturn(False) == 0 and board0[clickedsquare][0] == "w") or changeturn(False) == 1 and board0[clickedsquare][0] == "b":
                moveable = ml
                redraw(moveable)
                clicked = [True, clickedsquare]
    if clicked[0]:
        if clickedsquare in moveable: #can move rule come here
            #moved
            board0[clickedsquare] = board0[clicked[1]]
            board0[clicked[1]] = "00"
            click = [False, -1]
            moveable = []
            redraw(moveable)
            changeturn(True)
changeturn("start")
main()
turtle.onscreenclick(click)
screen.mainloop()