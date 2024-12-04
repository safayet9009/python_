n = int(input("Enter a number: "))

# Check if n is less than 2, as prime numbers are greater than 1
if n < 2:
    print(f"{n} is not a prime number.")
else:
    is_prime = True
    i = 2
    while i * i <= n:  # Only check up to the square root of n
        if n % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")
