# Prompt user to enter numbers separated by spaces
numbers_input = input("Enter a set of numbers separated by spaces: ")

# Split the input string into individual numbers
numbers_str = numbers_input.split()

# Convert the numbers from strings to floats
numbers = []
for num_str in numbers_str:
    if num_str.strip():  # Check if the string is not empty
        numbers.append(float(num_str))

# Check if there are any numbers entered
if not numbers:
    print("No numbers provided.")
else:
    # Calculate the sum of the numbers
    total = 0
    for num in numbers:
        total += num

    # Calculate the average
    average = total / len(numbers)
    print("Average:", average)
