# Prompt the user for a positive integer
n = int(input("Enter a positive integer: "))

# Initialize the sum of even numbers
sum_even = 0

# Loop through numbers from 1 to n
for num in range(1, n + 1):
    # Check if the number is even
    if num % 2 == 0:
        # Add the even number to the sum
        sum_even += num

# Print the sum of even numbers
print(f"The sum of even numbers between 1 and {n} is {sum_even}.")
