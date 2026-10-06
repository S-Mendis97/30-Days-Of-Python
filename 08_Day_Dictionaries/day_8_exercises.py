print("\n### Exercise 8 ###")
print("------------------")

dog = {}
dog = {'Name': 'Ronja', 'Color': 'Black and Brown',
       'Breed': 'Terrier', 'Legs': 4, 'Age': 13}

print("Dog Details\n-----------")
print("Dog Name:", dog.get('Name'), "\nColor:", dog.get('Color'),
      "Breed:", dog.get('Breed'), "Number of legs:", dog.get('Legs'),
      "Age:", dog.get('Age'))



stud_dct = dict(first_name = 'Samindi', last_name = 'Mendis',
                gender = 'Female', age = 29, married = False,
                skills = ['MATLAB', 'Simulink', 'Python', 'C', 'SolidWorks'],
                country = 'Sri Lanka', city = 'Colombo',
                address = dict(address_line_1 = 'Street Name 9', address_line_2 = '38448, Wolfsburg'))

print("\n\nStudent Details\n---------------")

print("Length of student dictionary:", len(stud_dct))
print("\nList of skills:", stud_dct['skills'], "\nSkill set data type:", type(stud_dct['skills']))


new_skills = ['CATIA V5', 'Siemens NX', 'Autodesk Fusion 360']
stud_dct['skills'].extend(new_skills)

print("\nNew skills:", new_skills)
print("List of Skills after modification using .extend:", *stud_dct['skills'])

print("\nGet dictionary key as a list:", list(stud_dct.keys()))
print("Get dictionary values as a list:", list(stud_dct.values()))

print("\nChange dictionary to a list of tuples:", list(stud_dct.items()))

user_remove = input(f"\nFrom the following keys in the dictionary: {stud_dct.keys()}\nEnter the one you would like to delete: ")

if user_remove in stud_dct:
    stud_dct.pop(user_remove)
    print(f"Student dictionary after removing '{user_remove}':\n{stud_dct}")
else:
    print("That key does not exist.")

dct_del_num = int(input("\nPress:\n1 to delete dog dictionary\n2 to delete student dictionary\nUser number: "))

if dct_del_num == 1:
    del dog

    try:
        dog
    except NameError:
        print("Dog dictionary has been successfully deleted!")

elif dct_del_num == 2:
    del stud_dct
    try:
        stud_dct
    except NameError:
        print("Student dictionary has been successfully deleted!")

else:
    print("Invalid number. Terminating process.")