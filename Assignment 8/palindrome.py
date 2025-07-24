#Write a program to check if entered number is a palindrome or not.
def palindrome(num):
    reverse=0
    while(num!=0):
        a=num%10
        reverse=(reverse*10)+a
        num=num//10
    return reverse
num=int(input("Enter a number to check palindrome or not : "))
result=palindrome(num)
if(result==num):
    print("Number is a palindrome.")
else:
    print("The number is not palindrome.")
