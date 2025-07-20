#Write a program to convert days into years, weeks and days.
days=int(input("Enter number of days : "))
years=days//365
remain=days%365
weeks=remain//7
days=remain%7
print("Years",years)
print("Weeks",weeks)
print("Days",days)