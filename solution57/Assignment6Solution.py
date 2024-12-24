# Method 2: Using Nested Loops
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*', end=' ')
        print()

input_lines = int(input("Enter number of lines: "))  # Input number of lines
print_pattern(input_lines)
