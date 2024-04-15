# Dorlens Janvier week 2 question 6

#prompt the user to enter a number 
numberOfIterations = int(input("Enter the number of iteration: "))

# i did a function for the number of iterations 
def estimatePi (numberOfIterations):
    sum =0
    for i in range(numberOfIterations):
        denominator = 2 * i + 1
        term = (-1) **  i / denominator
        sum += term
        piEstimated = 4*sum
        return piEstimated
    #output the result 
result = estimatePi(numberOfIterations)
print("the estimated pi is:" , result)








