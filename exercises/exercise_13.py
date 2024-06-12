# Your solution to Exercise 13
n=int(input("Enter a 4 dgit or less number: "))
test=False
if 1000<=n<=9999:
    first_digit= n//1000
    second_digit= (n//100)%10
    third_digit= (n//10)%10
    fourth_digit= n%10
    test= (first_digit != second_digit or first_digit == 0 or second_digit == 0) and \
    (first_digit != third_digit or first_digit == 0 or third_digit == 0) and \
    (first_digit != fourth_digit or first_digit == 0 or fourth_digit == 0) and \
    (second_digit != third_digit or second_digit == 0 or third_digit == 0) and \
    (second_digit != fourth_digit or second_digit == 0) and \
    (third_digit != fourth_digit or third_digit == 0)
    print(test)
elif 100<=n<=999:
    first_digit= n//1000
    second_digit= (n//100)%10
    third_digit= (n//10)%10
    test= (first_digit != second_digit or first_digit == 0 or second_digit == 0) and \
          (first_digit != third_digit or first_digit == 0 or third_digit == 0) and \
          (second_digit != third_digit or second_digit == 0 or third_digit == 0) 
    print(test)
elif 10<=n<=99:
    first_digit= n//10
    second_digit= n%10
    test= (first_digit != second_digit or first_digit == 0 or second_digit == 0)
    print(test)
else:
    print(test)