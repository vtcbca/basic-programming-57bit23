def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test the function
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial_recursive(number)}")