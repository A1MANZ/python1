
# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Open the file in write mode and save prime numbers
with open("results.txt", "w") as file:
    for num in range(1, 251):
        if is_prime(num):
            file.write(str(num) + "\n")  # Write prime number to file
            
print("Results saved in the file 'results.txt'")


