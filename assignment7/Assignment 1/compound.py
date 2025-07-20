#Write a program to enter P, T, R and calculate Compound Interest.
p=int(input("Enter principal : "))
r=int(input("Enter rate : "))
t=int(input("Enter time: "))
CI=(p*(1+(r/100))*t)-p
print("Compound Interest is:",CI)