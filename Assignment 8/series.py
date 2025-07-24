#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n
def sumOfNum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
        return sum
def factorial(n):
    fact=1
    for i in range(1,n):
        fact=fact*i
        return fact
def series(n):
    
