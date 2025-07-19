# Level 3 Exercises
print("Level 3 Exercises:")

# Exercise 1: Convert ages to a set and compare lengths
print("Exercise 1:")
user_ages = [22, 19, 24, 25, 26, 24, 25, 24]
unique_ages = set(user_ages)

print("Converted to set:", unique_ages)
print("Length of list:", len(user_ages))
print("Length of set:", len(unique_ages))

if len(user_ages) > len(unique_ages):
    print("The list has more elements (with duplicates).")
else:
    print("The set has more elements (unexpected, check input).")


# Exercise 2: Explain the difference between string, list, tuple, and set
print("\nExercise 2:")

sample_string = "Hello, world"
print("String: A sequence of characters used to store text:", sample_string)

sample_list = ['Apples', 'Pizza', 42, 3.14]
print("List: An ordered, mutable collection of items:", sample_list)

sample_tuple = ('Banana', 'Bread', 99)
print("Tuple: Like a list, but immutable (cannot be changed):", sample_tuple)

sample_set = {'Math', 'Science', 'Math', 'Art'}
print("Set: An unordered collection of **unique** items:", sample_set)


# Exercise 3: Count unique words in a sentence using split and set
print("\nExercise 3:")
text = "I am a teacher and I love to inspire and teach people."
words = text.lower().replace(".", "").split()
unique_words = set(words)

print("Words in sentence:", words)
print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
