# Your solution to Exercise 12
four_digit= int(input("Enter a four-digit number: "))
first_digit= four_digit//1000
second_digit= (four_digit//100)%10
third_digit= (four_digit//10)%10
fourth_digit= four_digit%10
thousands = '*' if first_digit % 2 == 0 else str(first_digit)
hundreds = '*' if second_digit % 2 == 0 else str(second_digit)
tens = '*' if third_digit % 2 == 0 else str(third_digit)
ones = '*' if fourth_digit % 2 == 0 else str(fourth_digit)
reset= thousands+hundreds+tens+ones
print(reset)