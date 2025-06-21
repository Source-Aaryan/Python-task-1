#Write a Python program that does the following:
#1. Takes two number as input from the user.
#2 Performs the basic mathematical operations on these two numbers:
# addition
# substraction
# multiplication
# division
#3. Displays the results of each operation on the screen


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# for division:
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (cannot divide by zero)"



# Display results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


