# Task 1
x = 10  # Global variable

def show():
    x = 5  # Local variable inside show()
    print(x)  # Prints 5

show()         # Calls show(), prints local x = 5
print(x)       # Prints global x = 10

# Output:
# 5
# 10

# Task 2
def outer():
    x = 10  # Local variable inside outer()
    
    def inner():
        print(x)  # inner() doesn't have x, so it takes x from outer()
    
    inner()

outer()

# Output:
# 10

# Task 3
x = "global"  # Global variable

def outer():
    x = "outer"  # Local to outer()

    def inner():
        x = "inner"  # Local to inner(), does not affect x in outer()
    
    inner()
    print("outer:", x)  # Prints outer

outer()
print("global:", x)  # Prints global

