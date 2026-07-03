#WAP to input user's first name and print its length
name = input("Enter your first name: ")
length = len(name)
print("The length of your first name is:", length)

#WAP to find the occurence of 'S' in a string
string = input("Enter a string: : ")
count = string.count('S')
print("The occurence of 'S' in the string is:", count)

#WAP to grade students based on their marks
marks = int(input("Enter student's marks: "))
if marks >= 90 and marks<= 100:
    print("Grade: A")
elif marks >= 75 and marks < 90:
    print("Grade: B")
elif marks >= 60 and marks < 75:
    print("Grade: C")
elif marks >= 50 and marks < 60:
    print("Grade: D")
elif marks < 50 and marks >= 0:
    print("Grade: F")
else:
    print("Invalid marks entered.")

#WAP to check if a number entered by the user is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#WAP to find the greatest of 3 numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    if (num1 > num2) and (num1 > num3):
        print("The greatest number is:", num1)
    elif (num1 == num2) and (num1 > num3):
        print("The greatest number is: num1 and num2")
    elif (num1 == num3) and (num1 > num2):
        print("The greatest number is: num1 and num3")
    else:
        print("All numbers are equal.")
elif (num2 >= num1) and (num2 >= num3):
    print("The greatest number is:", num2)
elif (num3 >= num1) and (num3 >= num2):
    print("The greatest number is:", num3)

#WAP to check if a number is a multiple of 7 or not
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")
