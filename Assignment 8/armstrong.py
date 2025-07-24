#WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def count(num):
    count=0
    while(num!=0):
        num=num//10
        count+=1
    return count
def armstrong(num):
    dc=count(num)
    sum=0
    while(num!=0):
        a=num%10
        num=num//10
        sum = sum + (a**dc)    
    return sum

num=int(input("Enter a number : "))
result=armstrong(num)
if(result==num):
    print("The number is Armstrong number . ")
else:
    print("The number is not Armstrong number . ")