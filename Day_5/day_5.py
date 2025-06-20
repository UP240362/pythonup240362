#1 Declare an empty list
empty_list = []

#2 Declare a list with more than 5 items
numbers = [1, 2, 3, 4, 5, 6]

#3 Find the length of your list
print("List length:", len(numbers))

#4 Get the first item, the middle item and the last item of the list
first_item = numbers[0]
middle_item = numbers[len(numbers) // 2]
last_item = numbers[-1]

#5 Declare a mixed data types list
mixed_data_types = ["Christopher", 24, 1.80, "Single", "Downtown"]

#6 Declare a list of IT companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#7 Print the list
print(it_companies)

#8 Print the number of companies
print(len(it_companies))

#9 Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

#10 Modify the first company and print the list
it_companies[0] = "Meta"
print(it_companies)

#11 Add another company to the list
it_companies.append("Tesla")

#12 Insert a company in the middle of the list
it_companies.insert(len(it_companies) // 2, "Nvidia")

#13 Change all company names to uppercase except 'IBM'
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()

#14 Join the companies with '#;  '
joined_companies = '#;  '.join(it_companies)

#15 Check if a certain company exists in the list
company_exists = "Google" in it_companies

#16 Sort the list alphabetically
it_companies.sort()

#17 Reverse the list
it_companies.reverse()

#18 Slice the first 3 companies
first_three = it_companies[:3]

#19 Slice the last 3 companies
last_three = it_companies[-3:]

#20 Slice the middle company or companies
middle = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    middle_companies = it_companies[middle - 1:middle + 1]
else:
    middle_companies = it_companies[middle:middle + 1]

#21 Remove the first company
it_companies.pop(0)

#22 Remove the middle company (or two if even number)
if len(it_companies) % 2 == 0:
    it_companies.pop(middle - 1)
    it_companies.pop(middle - 1)
else:
    it_companies.pop(middle)

#23 Remove the last company
it_companies.pop()

#24 Clear the list
it_companies.clear()

#25 Delete the list
del it_companies

#26 Merge front-end and back-end lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

#27 Insert Python and SQL after Redux
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')

#Print the full stack list
print(full_stack)
 # Exercise Leve 2

 #1 List of ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sort the list
ages.sort()

#Find min and max ages
min_age = min(ages)
max_age = max(ages)

#2 Add min and max age again to the list
ages.append(min_age)
ages.append(max_age)

#3 Find the median age
n = len(ages)
if n % 2 == 0:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
else:
    median_age = ages[n // 2]

#4 Find the average age
average_age = sum(ages) / len(ages)

#5 Find the range of the ages
age_range = max_age - min_age

#6 Compare (min - average) and (max - average) using abs()
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)

#7 List of countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

#8 Find the middle country
num_countries = len(countries)
if num_countries % 2 == 0:
    middle_countries = countries[num_countries // 2 - 1:num_countries // 2 + 1]
else:
    middle_countries = countries[num_countries // 2]

#9 Divide the list into two equal parts
if num_countries % 2 == 0:
    first_half = countries[:num_countries // 2]
    second_half = countries[num_countries // 2:]
else:
    first_half = countries[:num_countries // 2 + 1]
    second_half = countries[num_countries // 2 + 1:]

#10 Unpack the first 3 countries and group the rest as Scandinavian countries
first_country, second_country, third_country, *scandinavian_countries = countries

#Print results
print("Sorted ages:", ages)
print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Min to average difference:", min_diff)
print("Max to average difference:", max_diff)
print("Middle country(ies):", middle_countries)
print("First half of the list:", first_half)
print("Second half of the list:", second_half)
print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandinavian countries:", scandinavian_countries)
