# simple intrest using formula
p = 50000
t = 5
r = 3.5
si = p*t*r/100
print("simple interest:",si)

# Temperature
c = 37
farhrenheit = (c * 9/5)+ 32
print("farhrenheit:" , farhrenheit)

# Average of numbers
a = 12
b = 20
c = 30
average = (a+b+c)/3
print("average:" , average)

# Area of circle
f = 10
area = (22/7)*f*f
print("area:",area)

#swapping of numbers
a = 6
b = 5
a,b = b,a
print(a,b)




# def function_name(parameters):
#code block
#return result

#simple interest
def caluculate_simple_interest(p,t,r):
    si =p*t*r/100
    return si

    # calling the function
    print("simple interest:",
    caluculate_simple_interest (50000, 5, 3.5 ))

    #Temperature
    def celsius_to_fahrenheit(c):
       fahrenheit = (c * 9 / 5) + 32
       return farhrenheit
    print("fahrenheit:",celsius_to_fahrenheit(12))


    #Average of 3 numbers
    def find_average(a,b,c):
        average=(a+b+c)/3
        return average
    print("Average:",find_average(10,20,30))


    # Area of circle
    def area_of_circle(radius):
        pi = 22/7
        area = pi * radius * radius
        return area
        print("Area:",area_of_circle(10))


        #Swipping of numbers
        def swap_numbers(a,b):
             a, b = b, a
             return a, b
        a, b = swap_numbers(6, 5)
        print("after swapping:",a, b)

