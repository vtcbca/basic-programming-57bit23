def fibonacci_recursive(n, sequence=None):
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    if len(sequence) < 2:
        sequence.append(1 if len(sequence) else 0)
    sequence.append(sequence[-1] + sequence[-2])
    return fibonacci_recursive(n-1, sequence)

# Test the function
terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence (first {terms} terms): {fibonacci_recursive(terms)}")