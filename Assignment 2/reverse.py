#Write a program to reverse three-digit number.
num = int(input("Enter three digit number :" ))#128
a = num %10 #8
num = num // 10 #12
b = num % 10 # 2
reverse = (a*10)+b # 82
c = num // 10 # 1
reverse = (reverse*10)+c #821
print(reverse)
