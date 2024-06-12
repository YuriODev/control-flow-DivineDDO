# Your solution to Exercise 14
four=int(input("Enter a four-digit number: "))
first= four//1000
second= (four//100)%10
third= (four//10)%10
fourth= four%10
is_palindrome = (first == fourth) and (second== third)
print(is_palindrome)