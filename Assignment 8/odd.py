#Sum of all odd numbers between 1 to n
def odd(n):
    sum= 0
    for x in range(1, n + 1):
        if x % 2 != 0:
            sum += x
    return sum
    
                    
n=int(input("Enter a number : "))
result=odd(n)
print(result)
