# Simple Calculator in Python
def add(x, y): # This adds two values
    return x + y

def subtract(x, y): # This subtracts two values
    return x - y

def multiply(x, y): # This multiplies two values
    return x * y

def divide(x, y): # This divides two values
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

print("Select operation:") # Display options
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#User input
choice = input("Enter choice (1/2/3/4): ") 

num1 = float(input("Enter first number: ")) # Get first number
num2 = float(input("Enter second number: ")) # Get second number

if choice =='1': # Add operation
    print("Result:", add(num1, num2))
elif choice == '2': # Subtract operation
    print("Result:", subtract(num1, num2))
elif choice == '3': # Multiply operation
    print("Result:", multiply(num1, num2))
elif choice =='4': # Divide operation
    print("Result:", divide(num1, num2))
else:   # Invalid input
    print("Invalid input")
