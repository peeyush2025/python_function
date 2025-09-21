def swap_three_number(a,b,c):
    temp=a
    a=b
    b=c
    c=temp
x=int(input("enter first number(a):"))
y=int(input("enter first number(b):"))
z=int(input("enter first number(c):"))
x,y,z=swap_three_number(x,y,z)
print(f"after swapping:a{x},b={y},c={z}")