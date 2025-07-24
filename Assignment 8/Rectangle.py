#Write a program to calculate area of rectangle
def areaRect(l,b):
    area=l*b
    return area
l=int(input("Enter length of rectangle : "))
b=int(input("Enter breadth of rectangle : "))
result=areaRect(l,b)
print(result)