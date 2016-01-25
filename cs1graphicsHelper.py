from cs1graphics import *


def drawReferencePoints(canvas):
    ''' Loops through every element on a given canvas and marks the
    reference point of that element with a small orange circle'''

    for el in canvas.getContents():
        refPoint  = el.getReferencePoint()
        refMarker = Circle(5, refPoint)
        refMarker.setDepth(-999)
        refMarker.setFillColor('orange')
        canvas.add(refMarker)



def drawGrid(canvas, division = 100):

    width  = canvas.getWidth()
    height = canvas.getHeight()

    row = 0
    startY = 0
    while startY < width:

        startX = 0
        startY = row * division

        endX = width
        endY = startY

        line = Polygon(Point(startX,startY),Point(endX,endY))

        label = makeLabel(startX,startY)

        canvas.add(line)
        canvas.add(label)
        row += 1

    col = 0
    startX = 0
    while startX < height:

        startX = col * division
        startY = 0

        endX = startX
        endY = height

        line = Polygon(Point(startX,startY),Point(endX,endY))
        label = makeLabel(startX,startY)

        canvas.add(label)
        canvas.add(line)
        col += 1

def makeLabel(startX,startY):
    fontSize = 10
    label = Text(str(startX) + ',' + str(startY),fontSize)
    labelDimensions = label.getDimensions()
    label.adjustReference(-labelDimensions[0]/2,-labelDimensions[1]/2)
    label.moveTo(startX,startY)

    return label

def markClicks(canvas):

    while True:

        clickListener = canvas.wait();
        click = clickListener.getMouseLocation()

        x = int(click.getX())
        y = int(click.getY())

        label = Layer()

        cords = Text(str(x) + "," + str(y),10)
        cordDimensions = cords.getDimensions()
        cords.moveTo(x + cordDimensions[0]/2, y + cordDimensions[1]/2)
        cords.setFontColor('red')

        point = Circle(1, Point(x,y))

        label.add(cords)
        label.add(point)
        label.setDepth(-999)

        canvas.add(label)
