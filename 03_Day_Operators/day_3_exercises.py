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

triangle_perimeter = tri_a+tri_b+tri_c

print("Perimeter of triangle =", triangle_perimeter)