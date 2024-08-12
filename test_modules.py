# Ask user for circle radius
radius=float(input('Enter circle radius: '))

# import standard math module 
#import math 

# Import only pi constant
from math import pi


# Compute area of circle using pi constant
area=pi*radius**2

# Compute area of circle using pi constant from math module
#area=math.pi*radius**2


# Print area of circle using f-string
print(f'Area of circle: {area} au^2')