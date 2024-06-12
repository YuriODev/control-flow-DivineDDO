# Your solution to Exercise 7
first=float(input("Enter the first number: "))
second=float(input("Enter the second number: "))
arithmetic_option=input("Choose one of the following options: \n1. + \n2. - \n3. * \n4. / \n5. mod(Remainder division) \n6. pow(x to the power of) \n7. div(integer division)")
if arithmetic_option == "+":
    output=first+second
elif arithmetic_option == "-":
    output=first-second
elif arithmetic_option == "*":
    output=first*second
elif arithmetic_option == "/":
    if second == 0:
        output="Division by 0!"
    else:
        output=first/second
elif arithmetic_option == "mod":
    if second == 0:
        output="Division by 0!"
    else:
        output=first%second
elif arithmetic_option == "pow":
    output=first**second
elif arithmetic_option == "div":
    if second == 0:
        output="Division by 0!"
    else:
        output=first//second
else:
    output="Invalid option!"
print(output)