# Your solution to Exercise 2
child= int(input("Enter your age: "))
if child<=1 :
    print("You are an infant.")
elif child>1 and child<=12:
    print("You are a child.")
elif child >12 and child <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")