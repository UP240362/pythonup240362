import random

print("Level 3 Exercises")

# 1. Function that takes a list and returns a shuffled version
def shuffle_list(lst):
    lst_copy = lst[:]
    random.shuffle(lst_copy)
    return lst_copy

print("Shuffled list:", shuffle_list([1, 2, 3, 4, 5]))

# 2. Function that returns an array of 7 unique random numbers from 0 to 9
def generate_unique_random_seven():
    return random.sample(range(10), 7)

print("Unique random numbers:", generate_unique_random_seven())
