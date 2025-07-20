# To print Armstrong number within a given range
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))


for i in range(start , end+1):
    temp = i
    count = 0
    while(i != 0):
        a = i %10
        i = i//10
        count +=1
    i = temp
    sum = 0
    while(i != 0):
        a = i %10
        i //= 10
        sum = sum + (a**count)
    if(sum==temp):
        print(temp)
