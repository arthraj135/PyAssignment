
# Taking three numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
    
# Calculating the average of the three numbers
average = (num1 + num2 + num3) / 3
    
# Formatting the output message using % method
output_message = "The average of the three numbers is: %.2f" % average
    
# Displaying the result
print(output_message)

