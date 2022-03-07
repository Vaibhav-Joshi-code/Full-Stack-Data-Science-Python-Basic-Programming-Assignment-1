# Write a Python Program to print the area of a triangle
a = eval(input("Enter first side: "))
b = eval(input("Enter second side: "))
c = eval(input("Enter third side: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(f"The area of triangle with sides {a}, {b} and {c} is {area} sq units")
