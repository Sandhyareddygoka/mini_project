# what is a variables in python
#variables is like a container to store the data/can store numbers/to store the value.

name = "sandhya" # string variable
age = 23 # integer variable
height = 5.4 # float variable
print(name)
print(age)
print(height)


# Data types in python

# Numeric types
a = 10  
b = 5.6 
c = 3+2j 
print(type(a))
print(type(b))
print(type(c))


# Sequence type
name = "sandhya"
print(name[0])

# List 
fruits = ["Apple"," Banana","Mango"]
print(fruits[1])

# Tuples
colors = ("red","green","blue")
print(colors[2])

# String
message = "Hello , world!"
print(message)
print(type(message))

# mapping type
student = {"name":" sandhya","age":23}
print(student)
print(student["name"])
print(type (student))

# Set types
my_set = {1,2,3,4,5}
print(my_set)

# frozen set
normal_set = {1,2,3,4,2}
frozen = frozenset(normal_set)
print("frozenset:",frozen)
print("Type:", type(frozen))

# Boolean type
a = 10
b = 5
print(a>b)
print(a==b)




