print("Level 3 Exercises:")

# Exercise 1: Extract all countries containing the word 'land'
countries = ['Finland', 'Ireland', 'Switzerland', 'Iceland', 'New Zealand', 'Thailand']
countries_with_land = [country for country in countries if 'land' in country]
print("Countries containing 'land':", countries_with_land)

# Exercise 2: Reverse the list of fruits using a loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])
print("Reversed fruits list:", reversed_fruits)

# Exercise 3: Analyze data from countries_data.py
countries_data = [
    {
        'name': 'China',
        'population': 1409517397,
        'languages': ['Chinese']
    },
    {
        'name': 'India',
        'population': 1339180127,
        'languages': ['Hindi', 'English']
    },
    {
        'name': 'USA',
        'population': 324459463,
        'languages': ['English']
    },
    # ... more countries
]

# Total number of unique languages
unique_languages = set()
for country in countries_data:
    unique_languages.update(country['languages'])
print(f"Total unique languages: {len(unique_languages)}")

# Find the ten most spoken languages
from collections import Counter
language_counter = Counter()
for country in countries_data:
    for language in country['languages']:
        language_counter[language] += 1
top_languages = language_counter.most_common(10)
print("Top 10 most spoken languages:", top_languages)

# Find the 10 most populated countries
sorted_by_population = sorted(countries_data, key=lambda c: c['population'], reverse=True)
top_10_populated = sorted_by_population[:10]
print("Top 10 most populated countries:")
for country in top_10_populated:
    print(f"{country['name']} - Population: {country['population']}")
