#TurtleGraphics.py
#Name: Brennan Wood
#Date: 2/12/25
#Assignment: Lab 4 (All Combined)

import turtle #needed generally but not in CodeHS
# hideturtle() #hides the default turtle in CodeHS

kili = turtle.Turtle()
kili.shape("turtle")

# Drawing a square
def drawSquare(kili, size):
    for i in range(4):
        kili.forward(size)
        kili.right(90)
        
# Drawing a polygon
def drawPolygon(kili, sides):
    for i in range(sides):
        kili.forward(100)
        kili.right(360/sides)
        
        
# Defining a filled square
def fillSquare(kili):
    kili.begin_fill()
    drawSquare(kili, 50)
    kili.end_fill()
    
    
# Filled square function    
def fillCorner(kili, corner):
    drawSquare(kili,100)
    if corner == "1":
        fillSquare(kili)
    elif corner == "2":
        kili.up()
        kili.forward(50)
        kili.down()
        fillSquare(kili)
    elif corner == "3":
        kili.up()
        kili.right(90)
        kili.forward(50)
        kili.left(90)
        kili.down()
        fillSquare(kili)
    elif corner == "4":
        kili.up()
        kili.forward(50)
        kili.right(90)
        kili.forward(50)
        kili.left(90)
        kili.down()
        fillSquare(kili)
    else:
        kili.up()
        kili.backward(100)
        kili.write("Invalid corner!")
        
        
# Squares in squares

def smallerSquare(kili):
    kili.up()
    kili.forward(10)
    kili.right(90)
    kili.forward(10)
    kili.left(90)
    kili.down()
    
def squaresInSquares(kili, squares):
    for i in range(squares):
        size = 200
        step = size-i*20
        drawSquare(kili,step)
        smallerSquare(kili)
    
    
    

# asking the user to pick a function

shape = input("Please select a turtle action (polygon, fillCorner, squaresInSquares): ")

if shape == "polygon":
    sides = input("how many sides?: ")
    drawPolygon(kili, int(sides))
    
if shape == "fillCorner":
    corner = input("Which corner (1/2/3/4)?: ")
    fillCorner(kili,corner)
    
if shape == "squaresInSquares":
    squares = input("How many squares?: ")
    squaresInSquares(kili, int(squares))
    
