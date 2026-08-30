import math
def circle_stats(r):
    Area = round(math.pi * r**2 , 2)

    circumference = round(2 * math.pi * r , 2)

    return{Area, circumference}


print(circle_stats(3))