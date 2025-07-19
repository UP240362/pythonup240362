from collections import Counter

print("Level 3 Exercises")

# 1. Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))   # True
print(is_prime(10))  # False

# 2. Function to check if all elements in a list are unique
def all_unique(lst):
    return len(lst) == len(set(lst))

print(all_unique([1, 2, 3, 4]))      # True
print(all_unique([1, 2, 2, 4]))      # False

# 3. Function to check if all elements in a list are of the same type
def all_same_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(type(item) == first_type for item in lst)

print(all_same_type([1, 2, 3]))         # True
print(all_same_type([1, "2", 3]))       # False
print(all_same_type([]))               # True

# 4. Function to verify if a variable name is valid in Python
def is_valid_variable(name):
    reserved_words = {
        "False", "None", "True", "and", "as", "assert", "break", "class", "continue",
        "def", "del", "elif", "else", "except", "finally", "for", "from", "global",
        "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
        "return", "try", "while", "with", "yield"
    }
    return name.isidentifier() and name not in reserved_words

print(is_valid_variable("variable1"))   # True
print(is_valid_variable("1variable"))   # False
print(is_valid_variable("for"))         # False
print(is_valid_variable("my_var"))      # True

# Country data
country_data = [
    {"name": "China", "population": 1409517397, "languages": ["Chinese"]},
    {"name": "India", "population": 1339180127, "languages": ["Hindi", "English"]},
    {"name": "United States", "population": 324459463, "languages": ["English"]},
    {"name": "Indonesia", "population": 263991379, "languages": ["Indonesian"]},
    {"name": "Brazil", "population": 209288278, "languages": ["Portuguese"]},
    {"name": "Pakistan", "population": 197015955, "languages": ["Urdu", "English"]},
    {"name": "Nigeria", "population": 190886311, "languages": ["English"]},
    {"name": "Bangladesh", "population": 164669751, "languages": ["Bengali"]},
    {"name": "Russia", "population": 143989754, "languages": ["Russian"]},
    {"name": "Mexico", "population": 129163276, "languages": ["Spanish"]},
    {"name": "Japan", "population": 127484450, "languages": ["Japanese"]}
]

# Function: Most spoken languages
def most_spoken_languages(countries, top=10):
    language_counter = Counter()
    for country in countries:
        for language in country["languages"]:
            language_counter[language] += 1
    return language_counter.most_common(top)

print("Top 5 most spoken languages:")
print(most_spoken_languages(country_data, 5))
# Expected: [('English', 4), ('Chinese', 1), ('Hindi', 1), ('Indonesian', 1), ('Portuguese', 1)]

# Function: Most populated countries
def most_populated_countries(countries, top=10):
    sorted_countries = sorted(countries, key=lambda x: x["population"], reverse=True)
    return sorted_countries[:top]

print("Top 5 most populated countries:")
for country in most_populated_countries(country_data, 5):
    print(f'{country["name"]}: {country["population"]}')
