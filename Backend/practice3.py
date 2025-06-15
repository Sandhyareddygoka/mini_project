temp = float(input("Enter temperature in Celsius: "))

if temp < 15:
    print("Cold")
elif temp <= 25:
    print("Moderate")
else:
    print("Hot")