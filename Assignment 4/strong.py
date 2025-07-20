# To check if given number Strong Number.
num = int(input("Enter a number : "))
temp = num 
sum =0
while(num !=0 ):
    a = num%10 # seperate digit
    num = num // 10
    fact = 1   # give before starting loop
    for i in range (1 , a+1): # to find factorial of seperated digit
        fact = fact *i
    sum = sum + fact # to add fact of digits
if(sum == temp):
    print("The number is a strong number .")
else:
    print("The number is not a strong number .")