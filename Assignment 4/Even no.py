# To print all even numbers until n.
start = int(input("Enter start number : "))
end = int(input("Enter end number : "))
if(start > end):
    for x in range(start , end):
        if(x % 2 == 0):
            print(x)
else:
    for x in range (start , end-1):
        if(x % 2 == 0):
            print(x)
