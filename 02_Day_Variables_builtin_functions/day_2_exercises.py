### Exercise 2 ###
print("\nDay 2: 30 Days of python programming")
print("\n### Exercise 2 ###")
print("------------------")

# Level 1 & 2
print("Level 1 & 2\n-----------")
first_name = 'Samindi'
last_name = 'Mendis'
full_name = 'Samindi Methma Mendis'
country = 'Sri Lanka'
city = 'Colombo'
age = 29
year = 1997
is_married = False 
is_true = True
is_light_on = True

firstname, lastname, fullname, country2, city2, age2, year2, ismarried, istrue, islighton = 'Samindi', 'Mendis', 'Samindi Methma Mendis', 'Sri Lanka', 'Colombo', 29, 1997, False, True, True

print("First Name type ->", type(first_name))
print("Age type ->", type(age))
print("Is Married type ->", type(is_married))

print("\nFirst Name type ->", type(firstname), "\nAge type ->", type(age2), "\nIs Married type ->", type(ismarried))

print("\nLength of first name =", len(first_name))

print("Length of First Name:Length of Last Name ->", len(firstname), ":", len(lastname))

print("\n\nMathematical Calculations")
print("-------------------------")
num_one, num_two = 5, 4
print("num_one = ", num_one, "\nnum_two", num_two)

variable_total = num_one+num_two
variable_diff = num_one-num_two
variable_product = num_one*num_two
variable_division = num_one/num_two
variable_remainder = num_two%num_one
variable_exp = num_one**num_two
variable_floor_division = num_one//num_two

print("\nTotal = ", variable_total, "\nDifference = ", variable_diff, "\nProduct = ", variable_product, "\nDivision = ", variable_division,
      "\nRemainder = ", variable_remainder, "\nExponent = ", variable_exp, "\nFloor Division = ", variable_floor_division)

import numpy as np

print("\n\nCircle", "\n------")

radius = 30
area_of_circle = np.pi * (radius**2)
circum_of_circle = 2 * np.pi * radius

print("Radius of circle in m = ", radius, "\nArea of Circle = ", area_of_circle, "\nCircumference of Circle = ", circum_of_circle)

print("\n\nUser's Circle\n------------")
user_radius = int(input("Radius of circle in m = "))
user_area_of_circle = np.pi * (user_radius**2)

print("User's Radius = ", user_radius, "\nArea of User's Circle = ", user_area_of_circle)

print("\n\nUser Data\n---------")

user_first_name = input("First Name: ")
user_last_name = input("Last Name: ")
user_country = input("Country: ")
user_age = input("Age: ")

print("\nFull Name:", user_first_name, user_last_name, "\nCountry:", user_country, "\nAge:", user_age)