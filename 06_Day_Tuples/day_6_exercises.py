print("\n### Exercise 6 ###")
print("------------------")

print("\n\nLevel 1\n-------")

tpl1 = tuple()

brothers = ('Chanula', 'Fares', 'Hadi', 'Wassim')
sisters= ('Simona', 'Meline', 'Hannah')
siblings = brothers + sisters

print("Brothers:", brothers)
print("Sisters:", sisters)
print("\nNumber of Siblings:", len(siblings))

family_members = siblings + ('Dilrukshi', 'Shiral')

print("\nFamily Members:", family_members)

print("\n\nLevel 2\n-------")

print("Unpack siblings and parents:", *family_members)

fruits = ('apple', 'banana', 'cherry')
veggies = ('onion', 'mushroom', 'carrot', 'tomato')
animal_products = ('milk', 'eggs', 'cheese')

food_stuff_tp = fruits + veggies + animal_products
food_stuff_lt = list(food_stuff_tp)

print("\n\nFruits:", fruits, "\nVegetables:", veggies, "\nAnimal products:", animal_products)
print("\nFood stuff tuple:", food_stuff_tp)
print("Food stuff list:", food_stuff_lt)

if len(food_stuff_lt)%2 != 0:
    print("\nMiddle food item:", food_stuff_tp[int(len(food_stuff_tp)/2)])
else:
    print("\nMiddle food items:", food_stuff_tp[int(len(food_stuff_tp)/2)-1], "&", food_stuff_tp[int(len(food_stuff_tp)/2)])

print("First 3 items in food stuff list:", food_stuff_lt[:3])
print("Last 3 items in food stuff list:", food_stuff_lt[-3:])

print("\nDeleting food stuff tuple...")

del food_stuff_tp

try:
    food_stuff_tp

except NameError:
    print("Food stuff tuple deleted! Please refer to section to check method")
else:
    print("Food stuff tuple is not deleted!")
    print("If mushroom is in food stuff tuple:", 'mushroom' in food_stuff_tp)
    


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("\n\nNordic countries:", *nordic_countries)
print("Is Estonia a Nordic country?", 'Estonia' in nordic_countries)
print("Is Iceland a Nordic country?", 'Iceland' in nordic_countries)