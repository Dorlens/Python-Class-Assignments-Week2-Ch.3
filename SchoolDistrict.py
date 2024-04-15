# Dorlens Janvier Week 2 Chapter 3 Question 7


#Prompt the user 
startingSalary = float(input("Enter your starting salary $: "))
percentageIncreasePerYear = float(input("Enter your percentage increase per year: ")) /100
numberOfYears: int = int(input("Enter the number of years in the schedule: "))


#headers for year and salary 
print("years/salary")

# had to give it  giving an initial value for the for loop 
salary = startingSalary

# did a for loop so when the user inputs the starting salary and number of years and 
#increase of percentage it calculates up to that years the user inputs 
for years in range(1,numberOfYears + 1):
 print(f'{years}\t${startingSalary:.2f}')
salary*=(1+percentageIncreasePerYear)