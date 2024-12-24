# Method 2: Using Nested Loops for Numbers and Spaces
def print_triangle(n):
    for i in range(1, n+1):
        # Print leading spaces
        for j in range(n-i):
            print(" ", end="")
        # Print numbers
        for j in range(1, 2*i):
            print(j, end=" ")
        print()  # New line after each row

input_lines = int(input("Enter the number of rows: "))  # Input number of rows
print_triangle(input_lines)
