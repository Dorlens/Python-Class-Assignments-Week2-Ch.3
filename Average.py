#Dorlens Janvier week 2 Chapter 3 Question 9

number = input("Enter a number press enter when finish: ")
number= input("Enter a number press enter when finish: ")
number= input("Enter a number press enter when finish: ")

theSum=0.0 
while number !=" ":
    inputNumber = float(number)
    theSum += inputNumber
    number= input("Enter a number press enter when finish: ")
    break 

print(f'the sum of the number is {theSum}')