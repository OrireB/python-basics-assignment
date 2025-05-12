# Task 1: Variables & Data Types
# Declare variables of different data types: string, integer, float, boolean, list
# Print each variable along with its data type using the type() function

football_player = "Christian Ronaldo"         # string
jersey_number = 10                            # integer
height = 6.7                                  # float
is_player = True                              # boolean
place = ["London", "Saudi Arabia", "Spain"]          # list

# Print each variable along with its data type using the type() function
print(football_player, "-", type(football_player))
print(jersey_number, "-", type(jersey_number))
print(height, "-", type(height))
print(is_player, "-", type(is_player))
print(place, "-", type(place))


# Task 2: User Input & Conditional Statements
# Ask the user to input their age
# If age is 18 or above, print "You are eligible to vote."
# If age is below 18, print "You are not eligible to vote."

football_age = int(input("Enter your age: "))
if football_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are  not eligible to vote.")


# Task 3: Loops
# Write a for loop that prints numbers from 1 to 10
# Write a while loop that prints even numbers between 1 and 20

# For loop from 1 to 10
print("For loop from 1 to 10:")
for jersey_number in range(1, 11):
    print(jersey_number)

# While loop for even numbers from 1 to 20
print("Even numbers from 1 to 20:")
jersey_number = 1
while jersey_number <= 20:
    if jersey_number % 2 == 0:
        print(jersey_number)
    jersey_number += 1

# Task 4: Mini Challenge
# Create a list of 5 fruits
# Use a loop to print each fruit in uppercase letters
# If the fruit is "banana", skip it using continue

favourite_fruits = ["apple", "banana", "cherry", "mango", "grape"]

for fruit in favourite_fruits:
    if fruit == "banana":
        continue  # skip banana
    print(fruit.upper())
