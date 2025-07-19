# Exercises: Level 1
print("Level 1 Exercises:")

# Exercise 1: Create an empty tuple
print("Exercise 1:")
empty_tuple = tuple()
print("Empty tuple:", empty_tuple)


# Exercise 2: Create a tuple with your sisters' and brothers' names
print("Exercise 2:")
brothers = ("Jorge", "Andres", "Valentin")
sisters = ("Valentina",)
print("Brothers:", ", ".join(brothers))
print("Sisters:", ", ".join(sisters))


# Exercise 3: Join the tuples and assign them to 'siblings'
print("Exercise 3:")
siblings = (*brothers, *sisters)  # usando unpacking
print("My siblings are:", ", ".join(siblings))


# Exercise 4: Count how many siblings you have
print("Exercise 4:")
num_siblings = len(siblings)
print(f"I have {num_siblings} siblings.")


# Exercise 5: Add parents to the tuple and create 'family_members'
print("Exercise 5:")
parents = ("Mom Ana", "Dad Sergio")
family_members = list(siblings)  # convertir a lista para modificar fácilmente
family_members.extend(parents)
print("My full family is:", ", ".join(family_members))
