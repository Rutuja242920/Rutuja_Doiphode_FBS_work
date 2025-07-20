# To print all numbers in a range divisible by a given number.
start = int(input("Enter start number : "))
end = int (input("Enter end number : "))
num = int (input("Enter number through which you have divide : "))
for i in range(start , end+1):
    if(i%num ==0 ):
        print(i)
        