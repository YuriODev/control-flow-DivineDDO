# Your solution to Exercise 5
a=float(input("Enter a number coeffiecient for A: "))
b=float(input("Enter a number coeffiecient for B: "))
c=float(input("Enter a number coeffiecient for C: "))
d = b ** 2 - 4 * a * c
output= "No roots."
if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."
elif a == 0:
    if b != 0:
        output = f"{-c / b}"
elif b == 0:
    if c != 0:
        x1= ((-c/a)**0.5)
        x2= ((-(-c/a))**0.5)
        output = f"{x1} and {x2}"
    else:
        output= "0"
elif d>0:
    x1= (-b+ (b**2-4*a*c)**0.5)/(2*a)
    x2= (-b- (b**2-4*a*c)**0.5)/(2*a)
    output = f"{x1} and {x2}"
elif d==0:
    x= -b/(2*a)
    output = x
print(output)