print("\n### Exercise 10 ###")
print("------------------")

print("Level 1\n-------")

print("0 to 10 using for loop:")
for i in range(11):
    print(i)


print("\n0 to 10 using while loop:")
i = 0

while i <= 10:
    print(i)
    i += 1


print("\n10 to 0 using for loop:")
for i in range(10, -1, -1):
    print(i)


print("\n10 to 0 using while loop:")
i = 10

while i >= 0:
    print(i)
    i -= 1


print("\nTriangle:")
for i in range(1, 8):
    print("#" * i)


print("\nSquare:")
for row in range(8):
    for column in range(8):
        print("#", end=" ") # end=" " -> Says don't go to the next line yet; put a space after the # instead

    print() #  Starts new line for new row


library_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

print()
for item in library_list:
    print("Library:", item)

print()
for item_no in range(1,len(library_list)+1):
    print("Libraries:", ", ".join(library_list[:item_no]))


even_nums_1 = []; odd_nums_1 = []

for num in range(100+1):
    if num%2 == 0:
        even_nums_1.append(num)
    else:
        odd_nums_1.append(num)

print("\nEven Numbers:", even_nums_1); print("Odd numbers:", odd_nums_1)



print("\n\nLevel 2\n-------")

nums = []; even_nums_2 =[]; odd_nums_2 = []

for num_2 in range(101):
    nums.append(num_2)

    if num_2%2 == 0:
        even_nums_2.append(num_2)
    else:
        odd_nums_2.append(num_2)
    
print("Sum of all numbers between 0 and 100 =", sum(nums))
print("Sum of all even numbers between 0 and 100 =", sum(even_nums_2))
print("Sum of all even numbers between 0 and 100 =", sum(odd_nums_2))



print("\n\nLevel 3\n-------")

fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_reversed = []

for i in range(len(fruits)-1,-1,-1):
    fruits_reversed.append(fruits[i])

print("Reversed fruit list:", fruits_reversed)