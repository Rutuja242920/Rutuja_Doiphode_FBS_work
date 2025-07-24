#Write a program to find print the following Fibonacci series using
#functions:
#1 1 2 3 5 8 n terms
def Fibonacci():
    n=int(input("Enter number of terms : "))
    a=0
    b=1
    for i in range(n):
        if (a>n):
            break
        print(a,end='  ')
        c=a+b
        a=b
        b=c
Fibonacci()
