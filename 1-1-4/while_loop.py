num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
while num1 != num2:
    print("you didn't enter the same number")
    print("Please enter a valid response")
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))

print("You got it!")