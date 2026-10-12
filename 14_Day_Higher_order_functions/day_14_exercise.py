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



import sys
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
sys.path.append(str(project_folder))

from data.countries import countries as countries_list

def categorize_countries(pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(), countries_list))

print("\n12. Countries with:\nland in it:", ", ".join(categorize_countries('land')))
print("\nia in it:", ", ".join(categorize_countries('ia')))
print("\nisland in it:", ", ".join(categorize_countries('island')))
print("\nstan in it:", ", ".join(categorize_countries('stan')))



def countries_by_starting_letter(countries):
    starting_letters = {}

    for country in countries:
        first_letter = country[0].upper()

        if first_letter in starting_letters:
            starting_letters[first_letter] += 1
        else:
            starting_letters[first_letter] = 1

    return starting_letters

countr_start_letter = countries_by_starting_letter(countries_list)

print("\n13. Countries by starting letter:" )
for letter in countr_start_letter:
    print(letter, ":", countr_start_letter[letter])



from data.countries_data import countries_data 

def get_first_ten_countries(countr_data):
    return [country["name"] for country in countr_data[:10]] 

print("\n14. Get first 10 countries:", ", ".join(get_first_ten_countries(countries_data)))



def get_last_ten_countries(countr_data):
    return [country["name"] for country in countr_data[-10:]] 

print("\n15. Get last 10 countries:", ", ".join(get_last_ten_countries(countries_data)))






print("\n\nLevel 3\n-------")

from data.countries_data import countries_data as ctr_data

sorted_name = sorted(ctr_data, key = lambda item: item["name"])

print("Countries data list sorted by name:")
for country in sorted_name:
    print(country["name"], end=", ")



sorted_capital = sorted(filter(lambda country: country["capital"] != "", ctr_data), key=lambda country: country["capital"])

print("\n\nCountries data list sorted by capital:")
for country in sorted_capital:
    print(f"{country["capital"]} in {country["name"]}", end="\n")



sorted_population = sorted(ctr_data, key = lambda item: item["population"])

print("\nCountries data list sorted by population:")
for country in sorted_population:
    print(f"{country["population"]} in {country["name"]}", end="\n")



language_count = {}

for country in ctr_data:
    for language in country["languages"]:
        if language in language_count:
            language_count[language] += 1
        else:
            language_count[language] = 1


sorted_languages = sorted(
    language_count.items(),
    key=lambda item: item[1],
    reverse=True
)


top_10_languages = sorted_languages[:10]

print("\n10 most spoken languages by location:")

for language, count in top_10_languages:
    print(language, "-", count)



most_pplt_countr = sorted(ctr_data, key = lambda item: item["population"], reverse=True)

print("\n10 most populated countries:")
for country in most_pplt_countr[:10]:
    print(f"{country["name"]}: {country["population"]}")