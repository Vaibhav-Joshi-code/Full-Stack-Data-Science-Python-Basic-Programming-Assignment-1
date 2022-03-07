# Write a Python Program to swap two variables
a = eval(input("Enter any value: "))
b = eval(input("Enter any value: "))
print("Before swap: ")
print(f"a = {a}, b = {b}")

a,b = b,a
print("After swap: ")
print(f"a = {a}, b={b}")
