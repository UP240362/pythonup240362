#1Declarar variables
a=("Thirty")
b=("Days")
c=("of")
d=("Python")
e=("Coding")  
f=("For")
g=("ALL")
# Concatenar variables
oracion1 = a+" "+b+" "+c+" "+d
orcion2= e+" "+" "+f+" "+g
#2 Imprimir oraciones
print(oracion1)
print(orcion2)
#3 Delarar variable company  
company = ("Coding For All")
#4 imprimir la variable company
print(company)
#5 Print the length of the company string using len() method and print(). 
print("Longitud de la cadena company:", len(company))
#6 Change all the characters to uppercase letters using upper() method.
print(company.upper())
#7 Change all the characters to lowercase letters using lower() method.
print(company.lower())
#8 Use capitalize(), title(), swapcase() methods to format the string.
print(company.capitalize())
print(company.title())
print(company.swapcase())
#9 Cut(slice) out the first word of Coding For All string.
print(company[0:6]) 
#10 Check if Coding For All string contains the word Coding using the method index, find or other methods.
print("Coding" in company)
#11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))  
#12 Change Python for Everyone to Python for All using replace method.
print(company.replace("Pytthon for Everyone", "Python for All"))
#13 Split the string 'Coding For All' using space as the separator and print the list.
print(company.split())
#14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
#15 What is the character at index 0 in the string Coding For All.
print(company[0])
#16 What is the last index of the string Coding For All.
print(company[-1])
#17 What character is at index 10 in the string Coding For All.
print(company[10])
#18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
acronym = ("Python For Everyone")
name =  acronym.split()
space = ""
for acronym in acronym:
    space += acronym[0].upper()
print(acronym)
#19 Create an acronym or an abbreviation for the name 'Coding For All'.
name = "Coding For All"
words = name.split()
acronym = ""
for word in words:
    acronym += word[0].upper()
print(acronym)
#20 Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"
position = text.index("C")
print(position)
#21 Use index to determine the position of the first occurrence of F in Coding For All.
'Coding For All'.index('F')
#22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print('Coding For All People'.rfind('l'))

#23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

#24 Use rindex to find the position of the last occurrence of the word because in the following sentence:
print(sentence.rindex('because'))

#25 Slice out the phrase 'because because because' in the following sentence:
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

#26 Find the position of the first occurrence of the word 'because' in the following sentence:
print(sentence.find('because'))

#27 Slice out the phrase 'because because because' in the following sentence:
start = sentence.find('because')
end = sentence.rindex('because') + len('because')
print(sentence[start:end])

#28 Does 'Coding For All' start with a substring Coding?
print('Coding For All'.startswith('Coding'))

#29 Does 'Coding For All' end with a substring coding?
print('Coding For All'.endswith('coding'))

#30 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())

#31 Which one of the following variables return True when we use the method isidentifier():
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#32 The following list contains the names of some python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

#33 Use the new line escape sequence to separate the following sentences.
print("I am enjoying this challenge.\nI just wonder what is next.")

#34 Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

#35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {} meters square.".format(radius, int(area)))

#36 Make the following using string formatting methods:
a, b = 8, 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))













