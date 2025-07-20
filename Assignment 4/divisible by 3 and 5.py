# To print all integers upto n that aren’t divisible by 2 and 3.
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
for i in range(start , end ):
    if(i%2 != 0 and i%3 != 0):
        print(i)