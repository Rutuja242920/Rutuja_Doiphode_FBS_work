#Write a program to calculate area of circle
def circleArea(r):
    area=3.14*r**2
    return area
r=int(input("Enter radius of circle : "))
result=circleArea(r)
print(result)