#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter amount to be given to the shopkeeper : "))
#500 notes
n500 = amount // 500 #it will give number of notes
r_amount = amount % 500 #it will give remainning amount
# 200 notes
n200 = r_amount // 200
r_amount = r_amount % 200
# 100 notes
n100 = r_amount //100
r_amount = r_amount%100
#50 notes
n50 = r_amount // 50
r_amount = r_amount %50
#20 notes
n20 = r_amount//20
r_amount = r_amount%20
#10 notes
n10 = r_amount // 10
print("Number to notes to be given :")
print("Number of 500 notes",n500)
print ("Number of 200 notes",n200)
print("Number of 100 notes",n100)
print("Number of 50 notes",n50)
print("Number of 20 notes",n20)
print("Number of 10 notes",n10)