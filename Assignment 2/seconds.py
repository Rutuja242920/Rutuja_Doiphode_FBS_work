#Convert the time entered in hh,min and sec into seconds.
hh=int(input("Enter hours: "))
min=int(input("Enter minutes : "))
sec=int(input("Enter seconds: "))
sec=sec+(hh*3600)
sec=sec+(min*60)
print(sec)