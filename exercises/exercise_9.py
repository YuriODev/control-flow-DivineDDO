# Your solution to Exercise 9
three_digit= int(input("Enter a three-digit number: "))
first=three_digit//100
second=(three_digit//10)%10
third=three_digit%10
sum= first+third
if sum>second:
    print(">")
elif second>sum:
    print("<")
else:
    print("=")