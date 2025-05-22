# Initialize an empty list
user_list = []

# Ask the user how many numbers they want to enter
num_items = int(input("How many numbers would you like to enter? "))

# Get user input for each item and add it to the list
for i in range(num_items):
    item = input("Enter item {i + 1}: ")  # Ask for the input
    user_list.append(item)  # Add it to the list

# Print the list of items entered
print("\nYou entered the following list:")
print(user_list)

# Modify the list (for example, replace the first item)
if len(user_list) > 0:
    user_list[0] = input("\nEnter a new value to replace the first item: ")

# Remove an item from the list
item_to_remove = input("\nEnter an item to remove from the list: ")
if item_to_remove in user_list:
    user_list.remove(item_to_remove)
else:
    print(f"{item_to_remove} not found in the list!")

# Final list after modification
print("\nFinal list:")
print(user_list)
