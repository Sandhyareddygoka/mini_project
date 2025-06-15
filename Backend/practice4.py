def type_identifier(a,b,c):
    if(a==b==c):
        print("equalateral triangle")
    elif(a==b or a==c or b==c):
        print("isosceles triangle")
    else:
        print("scalene triangle")
type_identifier(2,2,2)
type_identifier(2,2,3)
type_identifier(2,3,5)