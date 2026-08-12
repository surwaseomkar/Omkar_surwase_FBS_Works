#Convert distant given in feet and inches into meter and centimeter

feet=int(input('enter a feet:'))
inches=int(input('enter a inches:'))
total_inches=(feet*12)+inches
meter=total_inches*0.0254
centimeter=meter*100
print(f'meter{meter},centimeter{centimeter}')