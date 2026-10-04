print("\nDay 5: 30 Days of python programming")
print("\n### Exercise 5 ###")
print("------------------")

print("\n\nLevel 1\n-------")

fruits = []
fruits = ['banana', 'apple', 'pineapple', 'mango', 'grape', 'lime', 'cherry']
print("Fruits =", fruits)
print('Length of fruits list =', len(fruits))

print("First fruit:", fruits[0], "\nMiddle fruit:", fruits[int(len(fruits)/2)], "\nLast fruit:", fruits[-1])

mixed_data_types = ['Samindi Mendis', 29, 164, 'Unmarried', 'address line 1, address line 2']
print(); print(mixed_data_types)

it_comp = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(); print(it_comp)
print("Number of Companies:", len(it_comp))
print("First company:", it_comp[0], "\nMiddle company:", it_comp[int(len(it_comp)/2)], "\nLast company:", it_comp[-1])

it_comp[0] = 'FaceBook'
print(); print(it_comp)

it_comp.append('IT Company 1')
print(); print(it_comp)

it_comp.insert(int(len(it_comp)/2),'IT Company 2')
print(); print(it_comp)

it_comp[1] = it_comp[1].upper()
print(); print(it_comp)

print("\nIs Microsoft in the IT company list? ->", 'Microsoft' in it_comp)

it_comp.sort()
print("Sorted IT Company List:",it_comp)

it_comp.reverse()
print("Reversed IT Company List:",it_comp)

it_comp_1 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_comp_2 = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'IT Company 1']


print("\nFirst 3 companies:", *it_comp[:3])
print("\nLast 3 companies:", *it_comp[-3:])

if len(it_comp_2)%2 == 0:
    print("\nIT Companies 2:", *it_comp_2)
    print("Middle IT companies:", it_comp_2[int(len(it_comp_2)/2)], "&", it_comp_2[int(len(it_comp_2)/2-1)])

if len(it_comp_1)%2 != 0:
    print("\nIT Companies 1:", *it_comp_1)
    print("Middle IT Company:", it_comp_1[int(len(it_comp_1)/2)])

    it_comp_1.pop(0)
    print("First IT Company removed:", it_comp_1)

    it_comp_1.pop(int(len(it_comp_1)/2))
    it_comp_1.pop(int(len(it_comp_1)/2))
    print("Middle IT Company removed:", it_comp_1)

    it_comp_1.pop(-1)
    print("Last IT Company removed:", it_comp_1)

    print("Clear all IT Companies:", it_comp_1.clear())

    #del it_comp_1
    #print("Destroy all IT Companies: ", it_comp_1)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

var_full_stack = front_end + back_end

print("\n\nFull Stack:", *var_full_stack)

full_stack = var_full_stack.copy()

redux_idx = full_stack.index('Redux')

full_stack.insert(redux_idx + 1, 'Python')
full_stack.insert(redux_idx + 2, 'SQL')

print("After inserting Python and SQL after Redux:", *full_stack)


print("\n\nLevel 2\n-------")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print("Ages list:", ages)

print("Sorted:", ages.sort())
print("Minimum age:", min(ages))
print("Maximum age:", max(ages))

ages += [min(ages)]+ [max(ages)]
print("Ages list:", ages)

print("Average age:", int(sum(ages)/len(ages)))
print(f'Range of ages: {min(ages)} - {max(ages)}')




