# Exercises: Level 2
print("Level 2 Exercises:")

# Exercise 1: Unpack siblings and parents from family_members
print("Exercise 1:")
family = ('Jorge', 'Fer', 'Miguel', 'Valeria', 'Mom Ana', 'Dad Sergio')
siblings_group = family[:4]
parents_group = family[4:]
print("Siblings:", siblings_group)
print("Parents:", parents_group)


# Exercise 2: Create fruits, vegetables and animal products tuples. Join them into one.
print("Exercise 2:")
fruits = ("Strawberry", "Watermelon", "Apple", "Melon", "Orange")
vegetables = ("Lettuce", "Lime", "Onion", "Broccoli", "Carrot")
animal_products = ("Milk", "Eggs", "Cheese")
food_items_tuple = fruits + vegetables + animal_products
print("food_items_tuple:", food_items_tuple)


# Exercise 3: Convert the tuple to a list
print("Exercise 3:")
food_items_list = list(food_items_tuple)
print("food_items_list:", food_items_list)


# Exercise 4: Slice out the middle item(s)
print("Exercise 4:")
middle_index = len(food_items_list) // 2
if len(food_items_list) % 2 == 0:
    middle_items = food_items_list[middle_index - 1: middle_index + 1]
else:
    middle_items = [food_items_list[middle_index]]
print("Middle items:", middle_items)


# Exercise 5: Slice out first and last three items
print("Exercise 5:")
first_three = food_items_list[:3]
last_three = food_items_list[-3:]
print("First three items:", first_three)
print("Last three items:", last_three)


# Exercise 6: Delete the tuple completely
print("Exercise 6:")
temp_tuple = tuple(food_items_list)
del temp_tuple
print("Tuple deleted. Attempting to use it will cause an error.")


# Exercise 7: Check if an item exists in the tuple
print("Exercise 7:")
item_to_check = "Cherry"
if item_to_check in food_items_tuple:
    print(f"{item_to_check} is in the tuple.")
else:
    print(f"{item_to_check} is NOT in the tuple.")


# Exercise 8: Check if 'Estonia' is a Nordic country
print("Exercise 8:")
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
country_check = 'Estonia'
if country_check in nordic_countries:
    print(f"{country_check} is a Nordic country.")
else:
    print(f"{country_check} is NOT a Nordic country.")


# Exercise 9: Check if 'Iceland' is a Nordic country
print("Exercise 9:")
if 'Iceland' in nordic_countries:
    print("'Iceland' is a Nordic country.")
else:
    print("'Iceland' is NOT a Nordic country.")
