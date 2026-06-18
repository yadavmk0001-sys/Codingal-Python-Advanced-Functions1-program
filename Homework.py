# 1. Take a number from the user
n = int(input("Enter a number: "))

# Create a list of odd numbers below the input value
odd_numbers = [i for i in range(1, n) if i % 2 != 0]

# Create a list of even numbers below the input value
even_numbers = [i for i in range(1, n) if i % 2 == 0]

print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)


# 2. Create a list of fruits
fruits = ["apple", "banana", "mango", "orange", "grapes"]

# Create a new list with the first letter capitalized
updated_fruits = [fruit.capitalize() for fruit in fruits]

print("Original fruits:", fruits)
print("Updated fruits:", updated_fruits)