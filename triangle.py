''' Henry Chan Write a a script which prompts user for three points of a triangle, draws the triangle with area and points printed if the points are valid; otherwise, an error message should be printed.'''

import math
from tkinter import Tk, Canvas

def distance(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    d = math.sqrt(dx**2 + dy**2)
    return d

def areaTriangle(x1,y1,x2,y2,x3,y3):
    side1 = distance(x1,y1,x2,y2)
    side2 = distance(x2,y2,x3,y3)
    side3 = distance(x3,y3,x1,y1)
    p = (side1 + side2 + side3)/2
    t1 = p-side1
    t2 = p-side2
    t3 = p-side2
    if t1==0 or t2==0 or t3==0:
        print("Does not form a triangle")
        return None
    area = math.sqrt( p*(p-side1)*(p-side2)*(p-side3) )
    return(area)

x1 = int( input("Please enter coordinate x1: ") )
y1 = int( input("Please enter coordinate y1: ") )
x2 = int( input("Please enter coordinate x2: ") )
y2 = int( input("Please enter coordinate y2: ") )
x3 = int( input("Please enter coordinate x3: ") )
y3 = int( input("Please enter coordinate y3: ") )

area = areaTriangle(x1, y1, x2, y2, x3, y3)
if area!=None:
    print("Area of your triangle is " + str(area) )
    points = [x1,y1, x2,y2, x3,y3]
    frame=Tk()
    canvas=Canvas(bg='black',height=250,width=300)
    coord=(100, 100, 200, 200)
    canvas.create_polygon(points, fill='white')
    canvas.pack()
    frame.mainloop()
