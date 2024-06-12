# Your solution to Exercise 3
enter=int(input("Enter a number from 1-36: "))
output="The bet will not play!"
if enter==0:
    print("Green")
elif 1<=enter<=10 :
    if enter%2==0:
        print("Black")
    else:
        print("Red")
elif 11<=enter<=18:
    if enter%2==0:
        print("Red")
    else:
        print("Black")
elif 19<=enter<=28:
    if enter%2==0:
        print("Black")
    else:
        print("Red")
elif 29<=enter<=36:
    if enter%2==0:
        print("Red")
    else:
        print("Black")
else:
    print(output)