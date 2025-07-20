#* * * * * 
#*       * 
#*       *
#*       *
#* * * * *
for i in range(1,6):
    for j in range(1,i+1):
        if(j==1 or i==5):
            print("*",end=' ')
        else:
            print( " ",end=' ')
   
    for j in range(1,6-i):
        if(i==1 or j==5-i):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()

