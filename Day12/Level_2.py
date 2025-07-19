import random

print("Level 2 Exercises")

# 1. Function that returns a list of hexadecimal colors
def list_of_hex_colors(n):
    colors = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colors.append(color)
    return colors

print("Hex Colors:", list_of_hex_colors(5))

# 2. Function that returns a list of RGB colors
def list_of_rgb_colors(n):
    colors = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f"rgb({r},{g},{b})")
    return colors

print("RGB Colors:", list_of_rgb_colors(5))

# 3. Unified color generator that returns hex or RGB colors based on input
def generate_colors(kind, amount):
    colors = []
    if kind == 'hex':
        for _ in range(amount):
            color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colors.append(color)
    elif kind == 'rgb':
        for _ in range(amount):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colors.append(f"rgb({r},{g},{b})")
    return colors

print("Generated Hex Colors (3):", generate_colors('hex', 3))
print("Generated Hex Color (1):", generate_colors('hex', 1))
print("Generated RGB Colors (3):", generate_colors('rgb', 3))
