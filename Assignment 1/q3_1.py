while True:
    # Asking the user to input a number or 'exit'
    user_input = input("Enter a number or 'exit' to quit: ")
        
    # Check if user wants to exit
    if user_input.lower() == 'exit':
        print("Exiting the program...")
        break
        
      # Check if input is a valid number
    if not user_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid number or 'exit'.")
        continue
        
    # Convert user input to float (to handle decimal numbers)
    number = float(user_input)

    # Determine if the number is positive, negative, or zero using if-elif-else statements
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
         print("The number is zero.")

