from math import remainder

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

while num1 % num2 != 0:
    print("these numbers are not evenly divisible")
    print("enter two divisible numbers")
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))

print("you did it!")



