def print_mirrored_triangle(height):
    for i in range(1,height+1):
        print(" "*(height-i)+ "*" * i)
height=int(input("enter the height of the triangle: "))
print_mirrored_triangle(height)