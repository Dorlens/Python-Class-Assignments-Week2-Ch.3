# Dorlens Janvier week 3 question 2


side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

# Did a if statement to make sure the user dont input a number less then 1
if side1 < 1:
   int(input( "Invalid number For Side 1 Enter a Number greater then 0: "))

if side2 < 1:
   int(input("Invalid number For Side 2 Enter a Number greater then 0: "))

if side3 <1:
   int(input("Invalid number For Side 3 Enter a Number greater then 0: "))

# so what i did was calculated the side to the 2 power for each side 
aSquared = side1**2
bSquared = side2**2
cSquared = side3**2

# i did a if to let the user know if it what they input was a right triangle or not 
if cSquared == aSquared + bSquared:
   print("The triangle with side lengths" , side1, side2 , "and ", side3 , "is a right triangle") 
else:
   print("The triangle with side lengths", side1, ",", side2, ", and", side3, "is not a right triangle.")