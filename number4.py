import math
import sys
from tkinter import Tk, Canvas

def triangleArea(x1,y1,x2,y2,x3,y3):
    area = abs((0.5)*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))
    return area

print("Please provide 3 points for the triangle: \
the x coordinate of a point should be a positive value and within 300, \
y coordinate should be a positive value and lesser than 200 ")
while 1:
    point1x = float(input( "Enter Point 1 x-coordinate : " )) 
    point1y = float(input( "Enter Point 1 y-coordinate : " )) 
    point2x = float(input( "Enter Point 2 x-coordinate : " )) 
    point2y = float(input( "Enter Point 2 y-coordinate : " )) 
    point3x = float(input( "Enter Point 3 x-coordinate : " )) 
    point3y = float(input( "Enter Point 3 y-coordinate : " )) 

    if (point1x>= 0 and point1y>= 0 and point2x>= 0 and point2y>= 0 and point3x>= 0 and point3y>=0 and point1x<= 300 and point1y<=200 and 
    point2x<= 300 and point2y<=200 and point3x<= 300 and point3y<=200):
        frame=Tk()
        canvas=Canvas(bg='black',height=250,width=300)
        coord_triangle=(point1x,point1y,point2x,point2y,point3x,point3y)
        canvas.create_polygon(coord_triangle,fill='red')
        coord_area = (150,170)
        coord_points = (150,190)
        area = triangleArea(point1x,point1y,point2x,point2y,point3x,point3y)
        area_string = "Area is: {}".format(area)
        points_string = "Points are: {},{},{},{},{},{}".format(point1x,point1y,point2x,point2y,point3x,point3y)


        canvas.create_text(coord_area,text=area_string,fill='white')
        canvas.create_text(coord_points,text=points_string,fill='white')

        canvas.pack()
        frame.mainloop()
        
    else:
        print("Points are invalid, please try again.")
        continue
        







