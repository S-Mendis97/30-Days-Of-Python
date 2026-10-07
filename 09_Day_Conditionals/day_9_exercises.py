print("\n### Exercise 9 ###")
print("------------------")

print("Level 1\n-------")

user_age_1 = int(input("Enter your age: "))

if user_age_1 >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {18-user_age_1} more year(s) to learn to drive")

my_age = int(input("\n\nEnter my age: "))
your_age = int(input("Enter your age: "))
age_diff = abs(my_age - your_age)


print()
if my_age > your_age:
    if age_diff == 1:
        print(f"I am {age_diff} year older than you :(")
    else:
        if age_diff == 1:
            print(f"I am {age_diff} year older than you :(")
        else:
            print(f"I am {age_diff} years older than you :(")

elif my_age == your_age:
    if age_diff == 1:
        print(f"I am {age_diff} year younger than you :D")
    else:
        print(f"I am {age_diff} years younger than you :D")
elif my_age < your_age:
    print(f"I am {your_age-my_age} years younger than you :D")



num_one = int(input("\n\nEnter number one: "))
num_two = int(input("Enter number two: "))

print()

if num_one > num_two:
    print(f"{num_one} is greater than {num_two}")
elif num_one < num_two:
    print(f"{num_one} is smaller than {num_two}")
elif num_one == num_two:
    print(f"{num_one} is equal to {num_two}")




print("\n\nLevel 2\n-------")

score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score. Please enter a number between 0 and 100.")
elif score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


winter = 'December', 'January', 'February'
spring = 'March', 'April', 'May'
summer = 'June', 'July', 'August'
autumn = 'September', 'October', 'November'

user_month = input("\n\nEnter month: ").capitalize()

if user_month in spring:
    print("It's spring season! Look at the birds and the bees!")
elif user_month in summer:
    print("It's summer time! Time to go to the beach!")
elif user_month in autumn:
    print("It's autumn season! Look at the beautiful colors around!")
elif user_month in winter:
    print("It's winter season! Brrrrr! Time for hot chocolate!")
else:
    print("Invalid month entered. Terminating process.")


fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("\n\nPlease enter a fruit: ").lower()

if user_fruit in fruits:
    print('That fruit already exist in the list. Fruit list:', *fruits)
else:
    print('That fruit is not currently in the list and is now being added...')
    fruits.append(user_fruit)
    print("New fruit list:", *fruits)



print("\n\nLevel 3\n-------")

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}


# 1. Check if skills exists and print the middle skill
if 'skills' in person:
    middle_index = len(person['skills']) // 2
    print("Middle skill:", person['skills'][middle_index])


# 2. Check if Python is one of the skills
if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python skill exists:", True)
    else:
        print("Python skill exists:", False)


# 3. Determine developer type
if 'skills' in person:
    skills = person['skills']

    if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
        print("He is a front end developer")

    elif all(skill in skills for skill in ['Node', 'Python', 'MongoDB']): # same thing as 'if 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:'
        print("He is a backend developer")

    elif all(skill in skills for skill in ['React', 'Node', 'MongoDB']):
        print("He is a fullstack developer")

    else:
        print("Unknown title")


# 4. Check marital status and country
if person['is_married'] and person['country'] == 'Finland':
    print(
        f"{person['first_name']} {person['last_name']} "
        f"lives in {person['country']}. He is married."
    )