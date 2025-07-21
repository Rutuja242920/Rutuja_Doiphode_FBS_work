n=int(input("Number of emp:"))
basic=int(input("Enter basic salary: "))
sum=0
for i in range(1,n):
    if(basic<20000):
        da=(basic*10)/100
        ta=(basic*12)/100
        hra=(basic*15)/100
        total=basic+da+ta+hra
        sum+=total
        print(sum)
        break
    else:
        da=(basic*15)/100
        ta=(basic*18)/100
        hra=(basic*20)/100
        total=basic+da+ta+hra
        
        sum+=total
        print(sum)

