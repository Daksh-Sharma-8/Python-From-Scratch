#WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
m1 = input("Enter the name of your favorite movie: ")
m2 = input("Enter the name of your second favorite movie: ")
m3 = input("Enter the name of your third favorite movie: ")

movies = [m1, m2, m3]

print("Your favorite movies are:", movies)

#WAP to check if a list contains a palindrome of elements.
l1 = [1, 2, 1]

copy_l1 = l1.copy()
copy_l1.reverse()

if(copy_l1 == l1):
    print("Palindrome")
else:
    print("Not a Palindrome")

#WAP to count the number of students with the "A" grade in the following tuple. ["C", "D", "A", "A", "B", "B", "A"] 
grades = ("C", "D", "A", "A", "B", "B", "A")
print("The number of students with the grade 'A' are: ", grades.count("A"))

#Store the above values in a list and sort them from "A" to "D".
grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print(grades)
