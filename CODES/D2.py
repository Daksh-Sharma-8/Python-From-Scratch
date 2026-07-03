#STRINGS IN PYTHON
#Escape Sequence Characters
print("Hello World") #Normal print statement
print("Hello\tWorld") #Tab space
print("Hello\nWorld") #New line
print("Hello\\World") #Backslash
print("Hello\'World") #Single quote
print("Hello\"World") #Double quote
print("Hello\bWorld") #Backspace
print("Hello\rWorld") #Carriage return
print("Hello\fWorld") #Form feed

#BASIC STRING OPERATIONS
#Concatenation
str1 = "Hello"
str2 = "World"
str3 = str1 + str2
print(str3) #Output: HelloWorld
str4 = str1 + " " + str2
print(str4) #Output: Hello World

#Length
len1 = len(str1)
print(len1) #Output: 5
len2 = len(str2)
print(len2) #Output: 5
len3 = len(str3)
print(len3) #Output: 10
len4 = len(str4)
print(len4) #Output: 11

#Indexing
print(str4[0]) #Output: H
print(str4[0:5]) #Output: Hello
print(str4[6:11]) #Output: World
print(str4[:3]) #Output: Hel                   #[0:3] means from index 0 to 2
print(str4[3:]) #Output: lo World              #[3:len(str4)] means from index 3 to the end of the string  
print(str4[:]) #Output: Hello World            #[0:len(str4)] means from index 0 to the end of the string
print(str4[2:len(str4)]) #Output: llo World
print(str4[-1]) #Output: d
print(str4[-5:-1]) #Output: Worl
print(str4[-4:]) #Output: orld

#STRING FUNCTIONS
str = "i am studying python"
print(str.endswith("on")) #Output: True
print(str.endswith("thOn")) #Output: False
print(str.startswith("i a")) #Output: true
print(str.startswith("Pyt")) #Output: False
print(str.capitalize()) #Output: I am studying python
print(str.replace("t", "r")) #Ouput: i am srudying pyrhon
print(str.replace("python", "java")) #Output: i am studying java
print(str.find("studying")) #Output: 5
print(str.find("o")) #Output: 18
print(str.find("not")) #Output: -1       #String not found
print(str.count("t")) #Output: 2
print(str.count("am")) #Output: 1

#CONDITIONAL STATEMENTS
age = 17
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
#Output: You are not eligible to vote

age = 19
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
#Output: You are eligible to vote

light = "red"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Light is broken")
#Output: Stop

light = "yellow"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Light is broken")
#Output: Wait

light = "green"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Light is broken")
#Output: Go

light = "blue"
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Wait")
elif light == "green":
    print("Go")
else:
    print("Light is broken")
#Output: Light is broken

