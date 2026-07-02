#PRINT
print("Hello World")

#VARIABLES
a = 2
b = 3
sum = a + b
print(sum)

#STRINGS
name = "Daksh"
print("Hello", name)

#OPERATORS
x = 10
y = 5

#Arithmetic Operators
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)            
print("Exponentiation:", x ** y)     
print("Floor Division: ", x // y)

#Comparision Operators
print("Equal: ", x == y)
print("Not Equal: ", x != y)
print("Greater than: ", x > y)
print("Less than: ", x < y)
print("Greater than or equal to: ", x >= y)
print("Less than or equal to: ", x <= y)

#Logical Operators
print("Logical AND: ", x > 5 and y < 10)
print("Logical OR: ", x > 5 or y < 10)
print("Logical NOT: ", not(x > 5 and y < 10))

#Assignment Operators
c = 10
d = c
print("Assignment: ", c)
c += 5
print("Add and Assign: ", c)
c = d
c -= 5
print("Subtract and Assign: ", c)
c = d
c *= 5
print("Multiply and Assign: ", c)
c = d
c /= 5
print("Divide and Assign: ", c)
c = d
c %= 5
print("Modulus and Assign: ", c)
c = d
c **= 5
print("Exponentiation and Assign: ", c)
c = d
c //= 5
print("Floor Division and Assign: ", c)
c = d

#TYPE CONVERSION
a = 5
b = 2.5
sum = a + b        # 5.0 + 2.5 = 7.5
print("Sum:", sum)

#Input
Name = input("Enter your Name: ")
print("Hello", Name)
Age = int(input("Enter your Age: "))
print("You are", Age, "years old.")
Weight = float(input("Enter your Weight (in KG): "))
print("Your Weight is", Weight, "KG.")
