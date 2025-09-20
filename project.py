import math
def caluculate_circumference(radius):
    return 2*math.pi*radius
radius=float(input("enter the radius of the circle: "))
circumference=caluculate_circumference(radius)
print(f"the circumference of the circle with radius{radius}is:{circumference:.2f}")