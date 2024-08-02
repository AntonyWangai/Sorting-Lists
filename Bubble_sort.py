def sort(numbers):
    length = len(numbers)
    # Perform length - 1 passes through the list
    for _ in range(length - 1):
        # Compare each element with the next one
        for x in range(length - 1):
            # If the current element is greater than the next, swap them
            if numbers[x] > numbers[x + 1]:
                numbers[x], numbers[x + 1] = numbers[x + 1], numbers[x]
    return numbers

# Get the number of items from the user
num = int(input("How many numbers do you want in your list\n"))

# Initialize an empty list
numbers = []
# Collect each number from the user
for i in range(num):
    x = int(input(f"Enter your item {i + 1}: "))
    numbers.append(x)

# Print the original list
print("Original list:", numbers)

# Sort the list and print the sorted list
print("Sorted list:", sort(numbers))


