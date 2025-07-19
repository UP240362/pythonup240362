import random
import string

print("Level 1 Exercises")

# 1. Function to generate a random user ID of six characters
def generate_random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=6))

print("Random User ID:", generate_random_user_id())

# 2. Function to generate multiple user IDs with user-specified length and quantity
def user_id_gen_by_user():
    num_chars = int(input("Number of characters per ID: "))
    num_ids = int(input("Number of IDs to generate: "))
    chars = string.ascii_letters + string.digits
    for _ in range(num_ids):
        print(''.join(random.choices(chars, k=num_chars)))

# Uncomment to use:
# user_id_gen_by_user()

# 3. Function to generate a random RGB color
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("Random RGB color:", rgb_color_gen())
