# To check if a given number is prime number or not.
num = int(input("Enter a Number : "))
for x in range(2,num):
    if(num % x == 0):
        print("Given number is not a prime number.")
        break
else:
    print("Given number is a prime number.")