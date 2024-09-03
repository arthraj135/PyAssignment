# Taking an integer input from the user
num = int(input("Enter an integer: "))
    
# Printing binary, octal, and hexadecimal equivalents using format() and bitwise operators
print(f"Decimal: {num}")
    
# Binary conversion using format() and bitwise operators
print("Binary: ", end="")
for i in range(31, -1, -1):  # 31 to 0 (32 bits in total)
    print((num >> i) & 1, end="")
print()  # newline after binary representation
    
# Octal conversion using format() and bitwise operators
print(f"Octal: {oct(num)}")
    
# Hexadecimal conversion using format() and bitwise operators
print(f"Hexadecimal: {hex(num)}")

