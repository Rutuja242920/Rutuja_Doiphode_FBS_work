#Write a program to check if entered year is a leap year or not.
def leap(year):
    if (year % 4 == 0):
        if ((year % 100 != 0) or (year % 400 == 0)):
            return True
    return False
year=int(input("Enter year : "))
result=leap(year)
if(result):
    print("It is a leap year.")
else:
    print("Not leap year")
