#WAP to print Fibonacci series upto n.
n=int(input("Enter number : "))
a=0
b=1
for i in range(n):
    if (a>n):
        break
    print(a,end=' ')
    c=a+b
    a=b
    b=c
