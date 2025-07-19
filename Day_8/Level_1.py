# Dictionary Exercises: Level 1
print("Level 1 Dictionary Exercises:")

# Exercise 1: Create an empty dictionary called dog
print("Exercise 1:")
dog = {}
print("Dog dictionary:", dog)


# Exercise 2: Add name, color, breed, legs, age to the dog dictionary
print("Exercise 2:")
dog = {
    'name': 'Tuco',
    'color': 'Blanco',
    'breed': 'Pastor Ingles',
    'legs': 4,
    'age': 6
}
print("Dog info:", dog)


# Exercise 3: Create a student dictionary with various keys
print("Exercise 3:")
student = {
    'first_name': 'Jorge',
    'last_name': 'Tavera',
    'gender': 'Male',
    'age': 19,
    'marital_status': 'Single',
    'skills': ['Python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': 'Circuito Paseo de los Cisnes 220'
}
print("Student dictionary:", student)


# Exercise 4: Get the length of the student dictionary
print("Exercise 4:")
print("Length of student dictionary:", len(student))


# Exercise 5: Get the value of skills and check the data type
print("Exercise 5:")
skills = student['skills']
print("Skills:", skills)
print("Data type of skills:", type(skills))


# Exercise 6: Add more skills to the list
print("Exercise 6:")
student['skills'].extend(['JavaScript', 'Node.js'])
print("Updated skills:", student['skills'])


# Exercise 7: Get dictionary keys as a list
print("Exercise 7:")
keys_list = list(student.keys())
print("Dictionary keys:", keys_list)


# Exercise 8: Get dictionary values as a list
print("Exercise 8:")
values_list = list(student.values())
print("Dictionary values:", values_list)


# Exercise 9: Convert dictionary to list of tuples using items()
print("Exercise 9:")
items_as_tuples = list(student.items())
print("List of (key, value) tuples:", items_as_tuples)


# Exercise 10: Delete one item from the dictionary
print("Exercise 10:")
student.pop('address')
print("Student dictionary after deleting 'address':", student)


# Exercise 11: Delete the entire dictionary
print("Exercise 11:")
print("Deleting student dictionary...")
del student
print("Student dictionary deleted.")
