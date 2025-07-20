#Write a program to enter P, T, R and calculate Compound Interest.
P=int(input("Enter principal : "))
T=int(input("Enter time : "))
R=int(input("Enter rate : "))
CI= (P * (1 + R / 100) ** T)-P

print(CI)