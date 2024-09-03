# Taking two numbers as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
    
# Checking if both numbers are even, odd, or one of each
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
else:
    print("One number is even and the other is odd.")