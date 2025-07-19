print("Level 2 Exercises:")

# Exercise 1: Sum all numbers from 0 to 100 using a for loop
total_sum = 0
for i in range(101):
    total_sum += i
print("The sum of all numbers from 0 to 100 is:", total_sum)

# Exercise 2: Sum even and odd numbers from 0 to 100 using a for loop
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("The sum of even numbers is:", even_sum)
print("The sum of odd numbers is:", odd_sum)
