# DAY 2 Functions $ Data Structures
#1.List
students=["Riya","Sayali","sakshi","Dhiraj"]
print("Students:",students)
print("First Student:",
students[0])
print("Number of Students:",
len(students))

#Add a student
students.append("Aditi")
print("After Adding:",students)

#2.Tuple
marks=(80,60,36,64)

print("Marks:",marks)
print("First Marks:",marks[0])
print("Number of Marks:",len(marks))

#3.Dictionary
student={
    "name":"Riya",
    "age":21,
    "course":"BCA",
    "marks":80
}
print("Student Detaile:",student)
print("Name:",student["name"])
print("course:",
student["course"])
print("marks:",student["marks"])

#4.For Loop
print("Student Names:")
for name in students:print(name)

#5.Functions
def greet(name):
    print("Hello",name)
greet("sakshi")

#Functions with calculation
def add_numbers(a,b):
    return a+b
result = add_numbers(20,10)
print("Addition:",result)

