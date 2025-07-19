# Level 1 Set Exercises
print("Level 1 Exercises:")

# Exercise 1: Find the length of the tech_companies set
print("Exercise 1:")
tech_companies = {'Instagram', 'Bing', 'Microsoft', 'Apple', 'Tesla', 'Cisco', 'Amazon'}
set_length = len(tech_companies)
print("The number of tech companies is:", set_length)


# Exercise 2: Add 'Twitter' to the set
print("Exercise 2:")
tech_companies_list = list(tech_companies)
tech_companies_list.append('Twitter')
print("After adding Twitter:", tech_companies_list)


# Exercise 3: Add multiple companies to the set
print("Exercise 3:")
tech_companies = set(tech_companies_list)
new_tech = {'Instagram', 'TikTok', 'WhatsApp', 'Spotify'}
tech_companies.update(new_tech)
print("After adding multiple companies:", tech_companies)


# Exercise 4: Remove one company from the set
print("Exercise 4:")
tech_companies.discard("Facebook")  # Using discard to avoid potential error
print("After removing Facebook:", tech_companies)


# Exercise 5: Difference between remove() and discard()
print("Exercise 5:")

print("- remove() deletes an element but causes an error if it's not found.")
try:
    sample_set = {'Facebook', 'Google', 'Microsoft'}
    sample_set.remove('Google')  # Works fine
    print("After remove('Google'):", sample_set)
    sample_set.remove('TikTok')  # This will raise an error
except KeyError as e:
    print(f"Error using remove(): {e}")

print("- discard() deletes an element and does nothing if it's not found.")
safe_set = {'Facebook', 'Google', 'Microsoft'}
safe_set.discard('Google')  # Works
safe_set.discard('TikTok')  # No error
print("After discards:", safe_set)
