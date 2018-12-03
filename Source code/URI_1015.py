

# Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) andp2 (x2, y2) and
# calculate the distance between them, 
# showing four decimal places after the comma,
# according to the formula:

# Distance = sqrt(((x2-x1)*2+(y2-y1)*2)

# Input
# The input file contains two lines of data. The first one contains two double 
# values: x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

# Output
# Calculate and print the distance value using the provided formula, with 4 digits after the decimal point.



                                                        # Solution
import math
value1 = input().split(" ")
value2 = input().split(" ")
x1,y1 = value1
x2,y2 = value2

Distance = math.sqrt((float(x2)-float(x1))*(float(x2)-float(x1))+(float(y2)-float(y1))*(float(y2)-float(y1)))

print("%0.4f"%Distance)

