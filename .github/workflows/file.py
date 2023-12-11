# Define a function to check if a number is prime.
def is_prime(number):
    # If the number is 1, it is not prime.
    if number == 1:
        return False
    # Iterate over all the numbers from 2 to the square root of the number.
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by any number from 2 to its square root, it is not prime.
        if number % i == 0:
            return False
    # If the number is not divisible by any number from 2 to its square root, it is prime.
    return True

# This program prints all the prime numbers between 1 and 250.
# The results are stored in a file called "results.txt".
# Create a list of all the numbers from 1 to 250.
numbers = list(range(1, 251))

# Iterate over the list of numbers.
for number in numbers:
    # Check if the number is prime.
    if is_prime(number):
        # Print the number.
        print(number)
        # Write the number to a file.
        with open("results.txt", "a") as file:
            file.write(str(number) + "\n")