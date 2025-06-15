USERNAME = "admin"
PASSWORD = "1234"

user = input("Enter username: ")
pwd = input("Enter password: ")

if user == USERNAME and pwd == PASSWORD:
    print("Access granted")
else:
    print("Access denied")