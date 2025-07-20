#Convert distant given in feet and inches into meter and centimeter.
feet=int(input("Enter distant in feet : "))
inches=int(input("Enter distant in inches : "))
meter =feet*0.3048+inches*0.0254
centimeter=(feet*30.48)+(inches*2.54)
print(meter)
print(centimeter)


