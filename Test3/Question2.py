n=int(input("Enter number of terms : "))

sum = 0
fact = 1

for i in range(1, n + 1):
    fact *= i  
    ans = i / fact
    sum += ans
print(sum)
