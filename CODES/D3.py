#LISTS
marks = [95.2, 46.8, 86.5, 65, 98.8]
print(marks)
print(marks[0])                        #Output: 95.2
print(len(marks))                      #Output: 5
student = ["Karan", 95.2, 18, "Delhi"] #List with mixed data types  / [Name, Marks, Age, City]
print(student)
student[1] = 98.8
print(student)                         #Marks updated to 98.8

#LIST SLICING
print(marks[1:4])
print(marks[:3])
print(marks[-3:-1])

#LIST METHODS
list = [2, 1, 3]
list.append(4)                         #Adds one element at the end
print(list)                            #Output: [2,1,3,4]
list.sort()                            #Sorts in ascending order
print(list)                            #Output: [1,2,3,4]
list.sort(reverse = True)              #Sorts in descending order
print(list)                            #Output: [4,3,2,1]
list.reverse()                         #Reverse List
print(list)                            #Output: [1,2,3,4]
list.insert(1, 5)                      #Insert element at index
print(list)                            #Output: [1,5,2,3,4]
l1= [1, 2, 8, 1, 5, 1]
l1.remove(1)                         #Removes the first occurence of element
print(l1)                            #Output: [2,8,1,5,1]
l1.pop(2)                            #Removes element at index
print(l1)                            #Output: [2,8,5,1]

#TUPLES
tup = (89, 25, 34, 56, 73, 95)
print(tup)                           #Output: (89, 25, 34, 56, 73, 95)
print(tup[1])                        #Output: 25
t1 = (1)
print(t1)                            #Output: 1
print(type(t1))                     #Output: <class 'int'>
t2 = (1,)
print(t2)                            #Output: (1,)
print(type(t2))                     #Output: <class 'tuple'>
t3 = ()
print(t3)                            #Output: ()
print(type(t3))                     #Output: <class 'tuple'>
t4 = ("Hello")
print(t4)                            #Output: Hello
print(type(t4))                     #Output: <class 'str'>
t5 = ("Hello",)
print(t5)                            #Output: ("Hello",)
print(type(t5))                      #Output: <class 'tuple'>
print(tup[1:4])                      #Output: (25, 34, 56)

#TUPLE METHODS
print(tup.index(25))                 #Returns index of first occurence / Output: 1
print(tup.count(95))                 #Counts total occurences   / Output: 1
