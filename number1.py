import math
import sys

def computeArea(radius):
    area = math.pi * radius * radius
    return area

radius = float(input( "Enter radius in feet : " )) 
area = computeArea(radius)
sys.stdout.write("The radius you provided was " + format(radius,'.2f') +" feet and the area is about " + format(area,'.2f') + " sq feet" )
