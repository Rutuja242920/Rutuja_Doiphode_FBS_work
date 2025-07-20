#Program to Find the Roots of a Quadratic Equation
a=int(input("Enter first value :"))
b=int(input("Enter second value:"))
c=int(input("Enter third value :"))
ans=(b*b)-(4*a*c)
ans=ans**0.5
root1=(-b+ans)/2*a
root2=(-b-ans)/2*a
print("Root1:",root1)
print("Root2:",root2)