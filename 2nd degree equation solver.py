import math

print("### WELCOME TO THE 2ND DEGREE EQUATION SOLVER ###")
a, b, c = map(float, input("Enter 'a', 'b', and 'c' separated by spaces (ex.: 2 -3 9): ").split())

while a == 0:
    a = float(input("'a' cannot be equal to 0 in a 2nd degree equation: Try again: "))

delta = (b**2) - (4 * a * c)

if delta > 0.0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Solution: x1 = {x1:g}, x2 = {x2:g}")
elif delta == 0.0:
    x = - (b / (2 * a))
    print(f"Solution: x = {x:g}")
else:
    x1 = complex(- (b / (2 * a)), (math.sqrt(-delta))/(2 * a))
    x2 = complex(- (b / (2 * a)), - (math.sqrt(-delta))/(2 * a))
    print(f"Solution: x1 = {x1}, x2 = {x2}")