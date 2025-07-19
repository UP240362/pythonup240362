import math

print("Level 1 Functions")

# 1. Sum of two numbers
def sum_two_numbers(a, b):
    return a + b

# 2. Area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# 3. Sum multiple numbers (with validation)
def sum_all_numbers(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    return "All elements must be numbers."

# 4. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# 5. Determine season by month
def get_season_by_month(month):
    month = month.lower()
    seasons = {
        "spring": ["march", "april", "may"],
        "summer": ["june", "july", "august"],
        "autumn": ["september", "october", "november"],
        "winter": ["december", "january", "february"]
    }
    for season, months in seasons.items():
        if month in months:
            return season.capitalize()
    return "Invalid month"

# 6. Calculate slope of a line
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (division by zero)."
    return (y2 - y1) / (x2 - x1)

# 7. Solve quadratic equation
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return "No real solutions."
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return x1, x2

# 8. Print elements of a list
def print_list_items(lst):
    for item in lst:
        print(item)

# 9. Reverse a list using a loop
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

# 10. Capitalize list items
def capitalize_list_items(lst):
    return [str(item).capitalize() for item in lst]

# 11. Add item to a list
def add_item_to_list(lst, item):
    lst.append(item)
    return lst

# 12. Remove item from a list
def remove_item_from_list(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

# 13. Sum all numbers up to N
def sum_up_to_n(n):
    return sum(range(n + 1))

# 14. Sum odd numbers up to N
def sum_odds_up_to_n(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)

# 15. Sum even numbers up to N
def sum_evens_up_to_n(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)
