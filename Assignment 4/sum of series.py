# To print sum of series upto n.
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
sum=0
for i in range(start , end+1):
    sum += i
print(sum)
