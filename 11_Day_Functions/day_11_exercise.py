print("\n### Exercise 10 ###")
print("------------------")

print("Level 1\n-------")

def add_two_numbers(num1, num2):
    num_sum = num1 + num2
    return num_sum

n1 = int(input("\nEnter number 1 = "))
n2 = int(input("Enter number 2 = "))

print(f"Summation of numbers {n1} and {n2} =", add_two_numbers(n1, n2))



import numpy as np

def area_of_circle(pi, r):
    cir_area = pi * r**2
    return cir_area

user_radius = int(input("\nEnter radius of circle = ")) 

print(f"Area of a circle with radius {user_radius} =", area_of_circle(pi = np.pi, r=user_radius))



def add_all_nums(*nums):
    total = 0

    for num in nums:
        if type(num) == int or type(num) == float:
            total += num
        else:
            return "All arguments must be numbers."

    return total



def convert_celcius_to_fahrenheit(temp_cel):
    temp_fahr = (temp_cel * 9/5) + 32
    return temp_fahr

t_cel = int(input("Enter temperature in °C = "))

print(f"{float(t_cel)}°C in Fahrenheit: {convert_celcius_to_fahrenheit(t_cel)}°F")



def check_season(month):
    if month in ['December', 'January', 'February']:
        return 'Winter'
    elif month in ['March', 'April', 'May']:
        return 'Spring'
    elif month in ['June', 'July', 'August']:
        return 'Summer!'
    elif month in ['September', 'October', 'November']:
        return 'Autumn'
    else:
        return 'Invalid month!'

user_month = input("Enter month: ")
user_month = user_month.capitalize()

print(f"Since the month is '{user_month}', the season is: {check_season(user_month)}")



def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        return "Slope is undefined"

    slope = (y2 - y1) / (x2 - x1)
    return slope

print("Slope is =", calculate_slope(1, 2, 3, 6))



def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return "No real solutions"

    x1 = (-b + discriminant**0.5) / (2*a)
    x2 = (-b - discriminant**0.5) / (2*a)

    return x1, x2

print("Quadratic equation solutions:", solve_quadratic_eqn(1, -3, 2))



def print_list(prt_lst):
    for item in prt_lst:
        print(item)

skills = ['Python', 'MATLAB', 'C', 'Java', 'HTML']

print_list(skills)



def reverse_list(my_list):
    reversed_list = []

    for item in my_list:
        reversed_list.insert(0, item)

    return reversed_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))



def capitalize_list_items(my_list):
    capitalized_list = []

    for item in my_list:
        capitalized_list.append(item.capitalize())

    return capitalized_list

print(capitalize_list_items(['python', 'numpy', 'pandas', 'django']))



def add_item(my_list, item):
    my_list.append(item)
    return my_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]

print(add_item(food_stuff, 'Meat'))
print(add_item(numbers, 5))



def remove_item(my_list, item):
    my_list.remove(item)
    return my_list



def sum_of_numbers(num):
    total = 0

    for i in range(num + 1):
        total += i

    return total

print(sum_of_numbers(5))    # 15
print(sum_of_numbers(10))   # 55
print(sum_of_numbers(100))  # 5050



def sum_of_odds(num):
    total = 0

    for i in range(num + 1):
        if i % 2 != 0:
            total += i

    return total

print(sum_of_odds(10))



def sum_of_even(num):
    total = 0

    for i in range(num + 1):
        if i % 2 == 0:
            total += i

    return total

print(sum_of_even(10))




print("\n\nLevel 2\n-------")

def evens_and_odds(num):
    even_count = 0
    odd_count = 0

    for i in range(num+1):
        if i%2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("\nThe number of odds are:", odd_count)
    print("The number of evens are:", even_count)

evens_and_odds(100)



def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

print()
print("Factoials of 5:", factorial(5))



def is_empty(value):
    if len(value) == 0:
        return True
    else:
        return False

print("\nAre given arguments empty?")
print("[]:",is_empty([]))
print("[1, 2, 3]:",is_empty([1, 2, 3]))
print("\"\":", is_empty(""))



def calculate_mean(my_list):
    return sum(my_list) / len(my_list)


def calculate_median(my_list):
    sorted_list = sorted(my_list)
    length = len(sorted_list)

    if length % 2 != 0:
        middle = length // 2
        return sorted_list[middle]

    else:
        middle1 = sorted_list[length // 2 - 1]
        middle2 = sorted_list[length // 2]
        return (middle1 + middle2) / 2


def calculate_mode(my_list):
    mode = None
    highest_count = 0

    for item in my_list:
        count = my_list.count(item)

        if count > highest_count:
            highest_count = count
            mode = item

    return mode


def calculate_range(my_list):
    return max(my_list) - min(my_list)


def calculate_variance(my_list):
    mean = calculate_mean(my_list)

    total = 0

    for num in my_list:
        total += (num - mean) ** 2

    return total / len(my_list)


def calculate_std(my_list):
    variance = calculate_variance(my_list)
    return variance ** 0.5

numbers = [1, 2, 2, 3, 4, 5]

print("\nMean:", calculate_mean(numbers))
print("Median:", calculate_median(numbers))
print("Mode:", calculate_mode(numbers))
print("Range:", calculate_range(numbers))
print("Variance:", calculate_variance(numbers))
print("Standard deviation:", calculate_std(numbers))



def greet(name="Guest"):
    print(f"Hello, {name}!")

print()
greet()
greet("Alice")



def show_args(**kwargs): # *args collects ordinary arguments into a tuple, where *kwargs collects named arguments into a dictionary
    for key, value in kwargs.items():
        print(key, ":", value)

print()
show_args(name="Alice", age=30, city="New York")





print("\n\nLevel 3\n-------")

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print()
print("Is 7 a prime number:",is_prime(7))
print("Is 10 a prime number:",is_prime(10))



def all_unique(my_list):
    return len(my_list) == len(set(my_list)) # set removes duplicates

print()
print("Are the elements in [1, 2, 3, 4] unqiue? ->", all_unique([1, 2, 3, 4]))     # True
print("Are the elements in [1, 2, 2, 4] unqiue? ->", all_unique([1, 2, 2, 4]))     # False



def same_data_type(my_list):
    if len(my_list) == 0:
        return True

    first_type = type(my_list[0])

    for item in my_list:
        if type(item) != first_type:
            return False

    return True

print("\nSame data type in [1, 2, 3]:", same_data_type([1, 2, 3]))
print("Same data type in [1, \"hello\", 3]", same_data_type([1, "hello", 3]))



import keyword

def valid_variable(variable):
    return variable.isidentifier() and not keyword.iskeyword(variable)

print("\nAre the following valid variable names?")
print("my_name:", valid_variable("my_name"))
print("2name:", valid_variable("2name"))
print("my-name:", valid_variable("my-name"))
print("for:", valid_variable("for"))