list=[23,25,28,34,35,38,39,40,42,108,112]
for i in list:
    if i%3==0:
        print(i)

list1 = ["apple","mango","pineapple","watermelon","orange","bluebarry","banana"]
for i in list1:
    if len(i)%2==0:
            print(i)
for i in list1:
    if "e" in i:
        print(i)
employee_details = [
    {'name': 'Mounika', 'salary': 29000, 'role': 'HR'},
    {'name': 'Sreeja', 'salary': 32000, 'role': 'Developer'},
    {'name': 'KiranKumar', 'salary': 35000, 'role': 'HR'},
    {'name': 'Rajesh', 'salary': 28000, 'role': 'Developer'},
    {'name': 'Anusha', 'salary': 31000, 'role': 'Tester'},
    {'name': 'Vikram', 'salary': 34000, 'role': 'Manager'},
    {'name': 'Trinath', 'salary': 30000, 'role': 'HR'}
]
for emp in employee_details:
    if emp["salary"]>=30000 and emp["role"]=="HR":
        print(emp)
for emp in employee_details:
    if emp['name'][0]==('A' or 'E' or 'I' or 'O' or 'U') and emp['salary']>30000:
        print(emp["name"])



    


