# Level 1 Exercises
print("Level 1 Exercises:")

# Exercise 1
print("Exercise 1:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# Exercise 2
print("Exercise 2:")
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
if my_age == your_age:
    print("We are the same age.")
elif my_age < your_age:
    difference = your_age - my_age
    print(f"You are {difference} year{'s' if difference > 1 else ''} older than me.")
else:
    difference = my_age - your_age
    print(f"I am {difference} year{'s' if difference > 1 else ''} older than you.")

# Exercise 3
print("Exercise 3:")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}.")
else:
    print("Both numbers are equal.")

# Level 2 Exercises
print("Level 2 Exercises:")

# Exercise 1
print("Exercise 1:")
grade = int(input("Enter your score: "))
if grade >= 80:
    print("Your grade is: A")
elif 70 <= grade <= 79:
    print("Your grade is: B")
elif 60 <= grade <= 69:
    print("Your grade is: C")
elif 50 <= grade <= 59:
    print("Your grade is: D")
else:
    print("Your grade is: F")

# Exercise 2
print("Exercise 2:")
month = input("Enter the month: ").capitalize()
if month in ['September', 'October', 'November']:
    print("The season is Autumn")
elif month in ['December', 'January', 'February']:
    print("The season is Winter")
elif month in ['March', 'April', 'May']:
    print("The season is Spring")
elif month in ['June', 'July', 'August']:
    print("The season is Summer")

# Exercise 3
print("Exercise 3:")
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print(f"Fruit added. Updated list: {fruits}")

# Level 3 Exercises
print("Level 3 Exercises:")

# Exercise 1
print("Exercise 1:")
person = {
    'first_name': 'Federico',
    'last_name': 'Yamal',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '20179'
    }
}

if 'skills' in person:
    mid_index = len(person['skills']) // 2
    print("Middle skill:", person['skills'][mid_index])
    if 'Python' in person['skills']:
        print("Skills include Python:", person['skills'])

skills_list = person.get('skills', [])
if 'JavaScript' in skills_list and 'React' in skills_list:
    print("He is a front end developer")
elif all(skill in skills_list for skill in ['Node', 'Python', 'MongoDB']):
    print("He is a backend developer")
elif all(skill in skills_list for skill in ['React', 'Node', 'MongoDB']):
    print("He is a fullstack developer")
else:
    print("Unknown title")

if person.get('is_married') and person.get('country') == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']} and is married.")

print("All exercises completed.")
