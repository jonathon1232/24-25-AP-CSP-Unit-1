num1 = int(input("please enter the grade you received"))


if num1 >= 90:
    print("your grade is A")
elif 80 <= num1 <= 89:
    print("your grade is B")
elif 70 <= num1 <= 79:
    print("your grade is C")
elif 65 <= num1 <= 69:
    print("your grade is D")
elif num1 < 65:
    print("you failed, try again next year!")