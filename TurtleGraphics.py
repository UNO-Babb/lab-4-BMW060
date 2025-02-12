#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

# Drawing a square
def drawSquare(kili, size):
    for i in range(4):
        kili.forward(size)
        kili.right(90)
        
# Drawing a polygon
def drawPolygon(kili, sides):
    for s in range(sides):
        kili.forward(100)
        kili.right(360/sides)
        
        
# Defining a filled square
def fillSquare(kili):
    kili.begin_fill()
    drawSquare(kili, 50)
    kili.end_fill()
    
    
# Filled square function    
def fillCorner(kili, corner):
    drawSquare(kili, 100)
    if corner == 1:
        fillSquare(kili)
    if corner == 2:
        kili.up()
        kili.forward(50)
        kili.down()
        fillSquare(kili)
    if corner == 3:
        kili.up()
        kili.right(90)
        kili.forward(50)
        kili.left(90)
        kili.down()
        fillSquare(kili)
    if corner == 4:
        kili.up()
        kili.forward(50)
        kili.right(90)
        kili.forward(50)
        kili.left(90)
        kili.down()
        fillSquare(kili)
        
        
# Squares in squares
def squaresInSquares(kili, squares):
    
    
    

def main():
    kili = turtle.Turtle()
    
    fillCorner(kili,4)
    
    # drawPolygon(kili,8)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
