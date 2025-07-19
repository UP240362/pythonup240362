# Level 2 Set Exercises
print("Level 2 Exercises:")

# Exercise 1: Join set_a and set_b
print("Exercise 1:")
set_a = {19, 22, 24, 20, 25, 26}
set_b = {19, 22, 20, 25, 26, 24, 28, 27}
union_set = set_a.union(set_b)
print("The union of A and B is:", union_set)


# Exercise 2: Find intersection of set_a and set_b
print("Exercise 2:")
common_elements = set_a & set_b  # Alternative syntax using &
print("Intersection of A and B is:", common_elements)


# Exercise 3: Is A a subset of B?
print("Exercise 3:")
is_subset = set_a <= set_b  # Alternative syntax for issubset()
print("Is A a subset of B?", is_subset)


# Exercise 4: Are A and B disjoint?
print("Exercise 4:")
are_disjoint = set_a.isdisjoint(set_b)
print("Are A and B disjoint sets?", are_disjoint)


# Exercise 5: Join A with B and B with A
print("Exercise 5:")
joined_a = set_a.copy()
joined_a.update(set_b)
joined_b = set_b.copy()
joined_b.update(set_a)
print("A updated with B:", joined_a)
print("B updated with A:", joined_b)


# Exercise 6: Symmetric difference and deletion of sets
print("Exercise 6:")
symmetric_diff = set_a.symmetric_difference(set_b)
print("Symmetric difference between A and B:", symmetric_diff)

# Deleting sets
del set_a
del set_b
print("Sets A and B have been deleted.")
