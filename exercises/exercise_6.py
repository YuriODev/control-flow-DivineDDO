# Your solution to Exercise 6
x1=float(input("Enter the x-coordinate of the first point: "))
y1=float(input("Enter the y-coordinate of the first point: "))
x2=float(input("Enter the x-coordinate of the second point: "))
y2=float(input("Enter the y-coordinate of the second point: "))
first_distance=x1**2 + y1**2
second_distance=x2**2 + y2**2
if first_distance<second_distance:
    print("B is further from the origin.")
elif first_distance>second_distance:
    print("A is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")