#Write a program to swap two numbers without using third variable.
num1=int(input("Enter value of num1 : "))
num2=int(input("Enter value of num2 : "))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)