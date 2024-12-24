def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor * divisor > n:  # Optimization
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

# Test the function
number = int(input("Enter a number: "))
if is_prime_recursive(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")