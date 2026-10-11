print("\n### Exercise 13 ###")
print("------------------")

print("Level 1\n-------")

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print("Numbers list:", numbers)
print("Only negatives and zero:", [i for i in numbers if i <= 0])



list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\nList of lists:", list_of_lists)
print("Flattened list:", [number for row in list_of_lists for number in row])



list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print("\nCreate list of tuples:" )

for row in list_of_tuples:
    print(row)



countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print("\nCountries list:", countries)
print("Flattened countries list:", [[tpl[0].upper(), tpl[0][:3].upper(), tpl[-1].upper()] for lst in countries for tpl in lst])

'''
Explanation for above code:

new_countries = []

print()
for lst in countries:
    for tpl in lst:
        new_countries.append([tpl[0].upper(), tpl[0][:3].upper(), tpl[-1].upper()])
    
print(new_countries)
'''



print("\nCountries list:", countries)
print("Countries dictionary:", [{'country': tpl[0].upper(), 'city' : tpl[-1].upper()} for lst in countries for tpl in lst])



names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

print("\nNames list:", names)
print("List of names concatenated:", [tpl[0]+ ' ' + tpl[-1] for lst in names for tpl in lst])



print("\nLambda function to solve slope or y-intercept of linear functions")

linear_function = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1),
    y1 - ((y2 - y1) / (x2 - x1)) * x1
)

print("Slope m, y-intercept b:", linear_function(1, 2, 3, 6))


print()