print("\n### Exercise 14 ###")
print("------------------")

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Level 1\n-------")

print("Countries list:", countries)
for country in countries:
    print(country)


print("\nNames list:", names)
for name in names:
    print(name)


print("\nNumber List:", numbers)
for number in numbers:
    print(number)





print("\n\nLevel 2\n-------")

def make_upper(country):
    return country.upper()

countries_upper = map(make_upper, countries)
print("1. Countries in uppercase using defined function:", list(countries_upper))


squared_numbers = map(lambda x: x**2, numbers)
print("\n2. Squared numbers using lambda function:", list(squared_numbers))


print("\n3. Names in uppercase using lambda function:", list(map(lambda name: name.upper(), names)))


def land_in_country(country):
    return 'land' in country

countries_with_land = filter(land_in_country, countries)
print("\n4. Countries with land in it using defined function:", list(countries_with_land))
print("4. Countries with land in it using lambda function:", list(filter(lambda country: 'land' in country, countries)))


print("\n5. Countries with exactly 6 characters:", list(filter(lambda country: len(country) == 6, countries)))


print("\n6. Countries with 6 characters or more:", list(filter(lambda country: len(country) >= 6, countries)))


print("\n7. Countries starting with E using lambda function:", list(filter(lambda country: country[0] == 'E', countries)))
print("7. Countries starting with E using .startswith('E'):", list(filter(lambda country: country.startswith('E'), countries)))


print("\n8. Chain two or more list iterators together (here: map and filter to find countries with land in it and make them uppercase):\n",
      list(map(lambda country: country.upper(), filter(lambda country: 'land' in country, countries))))



def get_string_lists(lst):
    return list(filter(lambda item: type(item) == str, lst))

mixed_list = ['Python', 5, 'MATLAB', 3.14, True, 'Simulink']

print("\n9. Mixed list:", mixed_list)
print("-> Only string items from mixed list:", get_string_lists(mixed_list))

from functools import reduce
print("\n10. Use reduce to sum all numbers in numbers list:", reduce(lambda x,y: x+y, numbers))



sentence = reduce(lambda x, y: x + ", " + y, countries[:-1])
sentence += f", and {countries[-1]} are north European countries."

print("\n11.", sentence)






print("\n\nLevel 3\n-------")


print()