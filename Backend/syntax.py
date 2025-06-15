# Basic  function
def fun1(x):
    print(x)

fun1(2)

#parameterized arugments
def fun2(x, y=10):
    return(x+y)
print(fun2(3,6))

# keyword arguments
def stud(name,rollno,quali):
    print(name,rollno,quali)

stud(rollno=20,quali='B tech',name='Goka Sandhya')

#Arbitary aruguments
def student(*details):
    print(details)
student("Goka Sandhya",20,'Hyderabad')

# Keyword-arbitay arguments
def mark_stu(**nums):
    print(nums)

mark_stu(name='Sandhya',cpa=6.76,qualify='Btech')

# Lambda function
sam = lambda x,y:x+y
print(sam(5,5))