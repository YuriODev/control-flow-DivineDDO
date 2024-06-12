# Your solution to Exercise 10
x1, y1=int(input("Enter a value for x1: ")), int(input("Enter a value for y1: "))
x2, y2=int(input("Enter a value for x2: ")), int(input("Enter a value for y2: "))
x3, y3=int(input("Enter a value for x3: ")), int(input("Enter a value for y3: "))
a= (x1-x2)**2 + (y1-y2)**2
b= (x2-x3)**2 + (y2-y3)**2
c= (x3-x1)**2 + (y3-y1)**2
if a==0 or b==0 or c==0 :
    print("No")
elif a+b==c or b+c==a or c+a==b:
    print("Yes")
else:
    print("No")