# from statistics import * : imports all the statistics modules. can directly use required function instead of, e.g. statistics.mean but instead mean
# import math : mathematical operations and constants. Have to use as e.g. math.pi to use operators. Else use from math import *


print("\n### Exercise 12 ###")
print("------------------")

print("Level 1\n-------")

import random
import string

def generate_random_user_id():
    
    characters = string.ascii_letters + string.digits
    user_id = ''

    for i in range(6):
        user_id += random.choice(characters)

    return user_id

print("Random user ID:", generate_random_user_id())


def user_id_gen_by_user(num_char, num_ids):

    characters = string.ascii_letters + string.digits

    user_ids_list = []

    for id_num in range(num_ids):
        user_id = ''
        
        for char in range(num_char):
            user_id += random.choice(characters)

        user_ids_list.append(user_id)

    return user_ids_list

user_char_num = int(input("\nNumber of characters in User-ID: "))
user_id_num = int(input("Number of User-IDs to be generated: "))


user_ids = user_id_gen_by_user(user_char_num, user_id_num)

print("User-IDs:"); print("\n".join(user_ids))


def rgb_color_gen():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)

    return f"\nrgb({red},{green},{blue})"


print(rgb_color_gen())





print("\n\nLevel 2\n-------")

def list_of_hexa_colors(num_colors):
    hex_char = string.hexdigits.lower()[:16]
    color_list = []

    for i in range(num_colors):
        color = '#'

        for j in range(6):
            color += random.choice(hex_char)

        color_list.append(color)

    return color_list

print("Hex color list:", list_of_hexa_colors(3))



def list_of_rgb_colors(num_colors):
    rgb_list = []

    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)

        color = f"rgb({red},{green},{blue})"
        rgb_list.append(color)

    return rgb_list

print("\nRGB color list:", list_of_rgb_colors(3))



def generate_colors(color_type, num_colors):
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)

    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)

    else:
        return "Invalid color type. Use 'hexa' or 'rgb'."

print("\nHexa or RGB colors:")
print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
print(generate_colors('rgb', 1))





print("\n\nLevel 3\n-------")

def shuffle_list(shuf_lst):
    random.shuffle(shuf_lst)
    return shuf_lst


my_list = ['Python', 'MATLAB', 'Simulink', 'SolidWorks', 'CATIA', 'Siemens NX', 'Fusion 360']

print("Unshuffled list:", my_list)
print("Shuffled list:", shuffle_list(my_list))



def seven_random_numbers():
    return random.sample(range(10),7)

print("\n7 random numbers:", seven_random_numbers())