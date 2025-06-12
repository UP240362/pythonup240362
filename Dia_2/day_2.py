#Day 2: 30 days of python programming
#Exercise 1: Level 1
first = 1
last = 2
full_name = 'Jorge Emiliano'
last_name = 'Tavera'
country = 'Mexico'
city = 'Mexico City'
age = 30
year = 2025
is_married = True
is_true = True
is_light_on = True
a,b,c = 1,2,3

          #Exercise 2: Level 2 
# 5. Check the data type of all your variables using type() built-in function
print(type(first))
print(type(last))
print(type(full_name))
print(type(last_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(a))
print(type(b))
print(type(c))

print("Length of first name:", len(full_name.split()[0]))

first_name_longitud = len(full_name.split()[0])
last_name_longitud = len(last_name)
print("Length of last name:", last_name_longitud)
print("Length of full name:", len(full_name))

num_one, num_two = 5, 4
total = num_one + num_two
print("Total:", total)
diff = num_one - num_two
print("Diff:", diff)
product = num_one * num_two
print("Product:", product)
division = num_one / num_two
print("Division:", division)
remainder = num_one % num_two
print("Remainder:", remainder)
exp = num_one ** num_two
print("Exponent:", exp)
#11
floor_division = num_one // num_two
print("Floor division:", floor_division)

# Área y circunferencia de un círculo con radio 30
radius = 30
area_of_circle = 3.141592653589793 * (radius ** 2)
circum_of_circle = 2 * 3.141592653589793 * radius
print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Tomar el radio como input del usuario y calcular el área
try:
    radio = float(input("Introduce el radio del círculo: "))
    area = 3.141592653589793 * (radio ** 2)
    print("Área del círculo con radio ingresado:", area)
except ValueError:
    print("Por favor, introduce un número válido para el radio.")

# Pedir datos al usuario
your_first_name = input("Introduce tu nombre: ")
your_last_name = input("Introduce tu apellido: ")
your_country = input("Introduce tu país: ")
your_age = input("Introduce tu edad: ")
print("Nombre:", your_first_name)
print("Apellido:", your_last_name)
print("País:", your_country)
print("Edad:", your_age)

# Mostrar palabras reservadas de Python
help('keywords')




