# memory pooling


a = 10
b = 10
print(a is b) # true same memory block used (pooled)

#string interning
a = "python"
b = "python"
print(a is b)# True interneed automatically

# Garbage collection
import gc
print(gc.isenabled())
gc.collect()


# mutable vs immutable
#mutable 
my_list = [1,2,3]
my_list.append(4) #modifies the existing 
print(my_list)

#immutable objects

name = "sandhya"
name = name + "reddy" # creates a new string 
print(name)
