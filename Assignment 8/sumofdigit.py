#Write a program to find sum of digits of a number.
def sumOfDigit( num):
    a=num%10
    num=num//10
    b=num%10
    c=num//10
    sum=a+b+c
    return sum
num=int(input("Enter a three digit number : "))
result=sumOfDigit(num)
print(result)
