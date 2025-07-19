print("Level 1 Exercises:")

# Exercise 1: Iterate from 0 to 10 using a for loop and a while loop
print("\nExercise 1:")
for num in range(11):
    print(num)

counter = 0
while counter <= 10:
    print(counter)
    counter += 1

# Exercise 2: Iterate from 10 to 0 using a for loop and a while loop
print("\nExercise 2:")
for num in range(10, -1, -1):
    print(num)

count = 10
while count >= 0:
    print(count)
    count -= 1

# Exercise 3: Print a right-angle triangle of # using a loop
print("\nExercise 3:")
for i in range(1, 8):
    print("#" * i)

# Exercise 4: Print an 8x8 grid of #
print("\nExercise 4:")
for row in range(8):
    print("#" * 8)

# Exercise 5: Print a multiplication pattern
print("\nExercise 5:")
for num in range(11):
    print(f"{num} x {num} = {num * num}")

# Exercise 6: Iterate through a list and print each item
print("\nExercise 6:")
technologies = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for tech in technologies:
    print(tech)

# Exercise 7: Print even numbers from 0 to 100
print("\nExercise 7:")
for num in range(0, 101, 2):
    print(num)

# Exercise 8: Print odd numbers from 0 to 100
print("\nExercise 8:")
for num in range(1, 101, 2):
    print(num)
