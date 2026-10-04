### Exercise 3 ###
print("\nDay 3: 30 Days of python programming")
print("\n### Exercise 3 ###")
print("------------------")

user_age = int(input("User Age: "))
print("\nUser age:", user_age, "\nUser age type:", type(user_age))

user_height = float(input("\nUser height in cm: "))
print("\nUser height in cm:", user_height, "\nUser height type:", type(user_height))

complex_number = 1+1j

print("\n\nTriangle\n--------")
print("Area\n----")
triangle_base = int(input("Enter triangle base: "))
triangle_height = int(input("Enter triangle height: "))
triangle_area = 0.5 * triangle_base * triangle_height

print("Area of triangle =", triangle_area)

print("\nPerimeter\n---------")
tri_a = int(input("Enter side a: "))
tri_b = int(input("Enter side b: "))
tri_c = int(input("Enter side c: "))

triangle_perimeter = tri_a + tri_b + tri_c

print("Perimeter of triangle =", triangle_perimeter)


print("\n\nRectangle\n--------")

print("Area & Perimeter\n----------------")
rect_length = int(input("Enter rectangle length: "))
rect_width = int(input("Enter rectangle width: "))

rect_area = rect_length*rect_width
rect_perimeter = 2 * (rect_length+rect_width)

print("\nArea of rectangle =", rect_area)
print("Perimeter of rectangle =", rect_perimeter)


print("\n\nCircle: Area & Circumference\n----------------------------")
import numpy as np

circ_radius = int(input("Enter radius of circle: "))

circ_area = np.pi * (circ_radius**2)
circ_circum = 2 * np.pi * circ_radius

print("\nArea of circle =", circ_area)
print("Circumference of circle =", circ_circum)


print("\n\nSlope and Euclidean Distance\n----------------------------")
x1, y1 = 2, 2; x2, y2 = 6, 10

slope = (y2 - y1)/(x2 - x1)
euclid_dist = (y2 - y1)**2 + (x2 - x1)**2

print("(x1,y1) =", (x1,y1), "\n(x2,y2) =", (x2,y2))
print("\nSlope = ", slope)
print("Euclidean Distance = ", euclid_dist)



for x in range(-100,100):
    y = x**2 + 6*x + 9 != 0
    if y == 0:
        print("For the equation: y = x**2 + 6*x + 9\ny = 0 at x =", x)
        break
    else:
        continue

python_length = len('python'); dragon_length = len('dragon')

print("\n\nPython length:", python_length, "\nDragon length:", dragon_length)
print("Python length != Dragon length ->", python_length!=dragon_length)

print("'on' is in Python and Dragon ->", 'on' in ('python' and 'dragon'))

print("\n'jargon' is in the sentence 'I hope this course is not full of jargon' ->", 'jargon' in 'I hope this course is not full of jargon')

print("\n'on' is not in Python and Dragon ->", 'on' not in ('python' and 'dragon'))

python_float = float(python_length)
python_string = str(python_float)

print("Python length:", python_length, "\nPython length to float:", python_float, "\nPython float to string:", python_string)

print("\nFloor division 7//3 = int(2.7) ->", 7//3==int(2.7))

print("\ntype('10') = type(10)? ->", type('10') == type(10))

print("\nint('9.8') = 10 ->", int(9.8) == 10)



print("\n\nPrinting Table\n--------------")
for num in range(1,6):
    print(num, 1, num, num**2, num**3)

print()