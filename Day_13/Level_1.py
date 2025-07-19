print("Level 1 Exercises")

# 1. Filter only negative numbers and zeros using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
non_positives = [n for n in numbers if n <= 0]
print("Non-positive values:", non_positives)

# 2. Flatten a 3D list into a 1D list
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sub1 in list_of_lists for sub2 in sub1 for num in sub2]
print("Flattened list:", flattened)

# 3. Create a list of tuples using list comprehension
tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("List of tuples:", tuples)

# 4. Transform nested list of country-capital pairs to a formatted list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def simplify_country_list(countries):
    result = []
    for group in countries:
        for country, capital in group:
            country_upper = country.upper()
            abbreviation = country_upper[:3]
            capital_upper = capital.upper()
            result.append([country_upper, abbreviation, capital_upper])
    return result

print("Simplified country list:", simplify_country_list(countries))

# 5. Convert nested country-capital list to a list of dictionaries
def convert_to_dicts(countries):
    result = []
    for group in countries:
        for country, city in group:
            result.append({
                'country': country.upper(),
                'city': city.upper()
            })
    return result

print("Country dictionaries:", convert_to_dicts(countries))

# 6. Convert nested name pairs to a list of concatenated strings
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def concatenate_names(name_list):
    return [f"{first} {last}" for group in name_list for first, last in group]

print("Concatenated names:", concatenate_names(names))

# 7. Lambda function to calculate slope and y-intercept of a line
def slope_intersection(x1, y1, x2, y2):
    return lambda x: (y2 - y1) / (x2 - x1) * (x - x1) + y1

# Example usage:
f = slope_intersection(1, 2, 3, 6)
print("Value at x = 4:", f(4))  # Should compute the y-value on the line for x=4
