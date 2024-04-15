# Week 2 chapter 3 question 1

# Declared the sides 
side1 = int(input("Enter side 1: "))
side2 = int(input("Enter side 2: "))
side3 = int(input("Enter side 3: "))

# Did a if statement to make sure the user dont input a number less then 1
if side1 < 1:
   int(input( "Invalid number For Side 1 Enter a Number greater then 0: "))

if side2 < 1:
   int(input("Invalid number For Side 2 Enter a Number greater then 0: "))

if side3 < 1:
   int(input("Invalid number For Side 3 Enter a Number greater then 0: "))
   
#This determines if the triangle is equilateral or not 
if side1 == side2 == side3:
   print("the triangle with side lengths" , side1, side2 , "and ", side3 , "is a an equilateral triangle")
else:
   print("the triangle with side lengths" , side1, side2 , "and ", side3 , "is a not equilateral triangle")

