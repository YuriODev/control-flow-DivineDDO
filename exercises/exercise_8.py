# Your solution to Exercise 8
three_digit= int(input("Enter a three-digit number: "))
digit= int(input("Enter a number from 0-9: "))
output= "False"
if 100>=three_digit>=999:
    print("The value is not a three-digit number.")
else:
    is_in_number = digit == three_digit % 10 or digit == (three_digit // 10) % 10 or digit == three_digit // 100

    print(is_in_number)