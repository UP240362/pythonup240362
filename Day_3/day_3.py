#Dia 3 30 days of paython
# Declarar variables
Age = 25 #integer
Height = 1.70 #float  
complex_Number = 5 + 2j #complex  

# Área de un triángulo
base = float(input("Escribe la base del triángulo: "))
height_Triangle = float(input("Escribe la altura del triángulo:"))
area_Triangle = 0.5 * base * height_Triangle
print("El área es: ", int(area_Triangle))

# Perímetro de un triángulo
a = float(input("Lado a: "))
b = float(input("Lado b: "))
c = float(input("Lado c: "))
perimeter= a + b + c
print("El perímetro es: ", int(perimeter))

# Área y perímetro de un rectángulo
long = float(input("Escribe el largo del rectángulo: "))
width = float(input("Escribe el ancho del rectángulo: "))
area_Rectangle = long * width
perimeter_Rectangle = 2 * (long + width)
print("Área del rectángulo:", area_Rectangle)
print("Perímetro del rectángulo:", perimeter_Rectangle)

# Área y circunferencia circulo
radius = float(input("Escribe el radio del círculo: "))
pi = 3.14
area_Circle = pi * radius ** 2
circumference = 2 * pi * radius
print("Área del círculo:", area_Circle)
print("Circunferencia del círculo:", circumference)

# Recta y = 2x - 2
slope1 = 2
interseccion_x = 2 / 2 
interseccion_y = -2     
print("Pendiente:", slope1)
print("Intersección eje x:", interseccion_x)
print("Intersección eje y:", interseccion_y)

#9 Pendiente y distancia euclidiana entre dos puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
slope2 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Pendiente entre los puntos:", slope2)
print("Distancia euclidiana:", distancia)

#10 Comparar pendientes
print("¿Las pendientes son iguales?", slope1 == slope2)

#11 Evaluar y = x^2 + 6x + 9 y hallar x cuando y = 0
value_x = [-3, -2, 0, 1]
for x in value_x:
  y = x**2 + 6*x + 9
  print(f"Cuando x = {x}, y = {y}")

#12 Comparar longitud de palabras
print(len("python") != len("dragon"))

#13 Verificar si 'on' está en ambas palabras
print('on' in 'python' and 'on' in 'dragon')

#14 Verificar si "jargon" está en la oración
oracion = "I hope this course is not full of jargon."
print("jargon" in oracion)

#15 Afirmación falsa: no hay 'on' en python ni en dragon
print('on' not in 'dragon' and 'on' not in 'python')

#16 Longitud de "python" a float y a string
length_Python = len("python")
print(float(length_Python))
print(str(length_Python))

#17 Número par
numero = int(input("Ingresa un número para verificar si es par: "))
print(numero % 2 == 0)

#18 Verificar división entera
print(7 // 3 == int(2.7))

#19 Verificar tipos
print(type('10') == type(10))

#20 Verificar conversión de cadena
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a entero directamente.")

#21 Calcular salario
hours= float(input("Escribe las horas trabajadas: "))
rate = float(input("Escribe tu tarifa por hora: "))
salary = hours * rate
print("Tu ingreso semanal es", int(salary))

#22 Calcular segundos vividos
years = int(input("Ingresa el número de años que has vivido: "))
seconds = years * 365 * 24 * 60 * 60
print(f"Has vivido {seconds} segundos.")

#23 Mostrar tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")