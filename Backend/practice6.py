age = int(input("Enter age: "))

if 0 <= age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 60:
    print("Adult")
else:
    print("Senior")