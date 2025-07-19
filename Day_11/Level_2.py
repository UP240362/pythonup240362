import math
from collections import Counter

print("Level 2 Exercises:")

# 1. Call your factorial function, takes an integer and returns its factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

# 2. Call your is_empty function, takes a parameter and checks if it's empty
def is_empty(value):
    return not bool(value)

print("Is empty (\"\"):", is_empty(""))      
print("Is empty ([]):", is_empty([]))      
print("Is empty (\"texto\"):", is_empty("texto"))

# 3. Functions for mean, median, mode, range, variance, and standard deviation
def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    middle = n // 2
    if n % 2 == 0:
        return (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        return sorted_data[middle]

def calculate_mode(data):
    count = Counter(data)
    max_freq = max(count.values())
    modes = [k for k, v in count.items() if v == max_freq]
    return modes[0] if len(modes) == 1 else modes

def calculate_range(data):
    return max(data) - min(data)

def calculate_variance(data):
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)

def calculate_std(data):
    return math.sqrt(calculate_variance(data))

# Example usage
sample_data = [1, 2, 2, 3, 4]

print("Mean:", calculate_mean(sample_data))
print("Median:", calculate_median(sample_data))
print("Mode:", calculate_mode(sample_data))
print("Range:", calculate_range(sample_data))
print("Variance:", calculate_variance(sample_data))
print("Standard Deviation:", calculate_std(sample_data))
