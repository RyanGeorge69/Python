# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Print the original list
print("Original list:", numbers)

# Access and print the first item
print("First item:", numbers[0])

# Change the second item
numbers[1] = 25
print("After changing second item:", numbers)

# Add a new number to the list
numbers.append(60)
print("After appending 60:", numbers)

# Remove a number from the list
numbers.remove(30)
print("After removing 30:", numbers)

# Print each number using a loop
print("All items in the list:")
for num in numbers:
    print(num)
