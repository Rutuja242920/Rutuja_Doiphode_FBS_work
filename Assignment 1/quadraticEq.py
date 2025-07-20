#Program to Find the Roots of a Quadratic Equation
a=int(input("Enter value of a : "))
b=int(input("Enter value of b : "))
c=int(input("Enter value of c : "))
ans=((b**b)-4*a*c)**0.5
root1=(-b+ans)/2*a
root2=(-b-ans)/2*a
print(root1)
print(root2)