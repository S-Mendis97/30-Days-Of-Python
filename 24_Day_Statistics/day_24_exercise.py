print("\n### Exercise 24: Statistics ###")
print("-------------------------------")

import numpy as np

python_list =[1,2,3,4,5]
print("Python list:", python_list)
print("Python list type:", type(python_list))

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
print("\n2D list:", two_dimensional_list)
print("2D list type:", type(two_dimensional_list))


print("\nInt Numpy Arrays\n----------------")
numpy_array_from_list = np.array(python_list)
print("Int numpy array from list:", numpy_array_from_list, "\nInt numpy array from list type:", type(numpy_array_from_list))


print("\nFloat Numpy Arrays\n------------------")
numpy_array_from_list2 = np.array(python_list, dtype=float)
print("Float numpy array from list:", numpy_array_from_list2, "\nFloat numpy array from list type:", type(numpy_array_from_list2))


print("\nBoolean Numpy Arrays\n--------------------")
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print("Boolean numpy array from list:", numpy_bool_array, "\nBoolean numpy array from list type:", type(numpy_bool_array))


print("\nCreating multidimensional array using numpy\n-------------------------------------------")
print("2D list:", two_dimensional_list)
print("2D list type:", type(two_dimensional_list))

numpy_two_dimensional_list = np.array(two_dimensional_list)
print("\nMultidimensional array from 2D list:\n", numpy_two_dimensional_list, "\nMultidimensional array type:", type(numpy_bool_array))


print("\nConverting numpy array to list\n------------------------------")
np_to_list = numpy_array_from_list.tolist()

print("Numpy array:", numpy_array_from_list,
      "\nNumpy array to list:", np_to_list,
      "\n\n2D numpy array:\n", numpy_two_dimensional_list,
      "\n2D np array to list:", numpy_two_dimensional_list.tolist())


print("\nCreating numpy array from tuple\n-------------------------------")

python_tuple = (1,2,3,4,5)
print("Python tuple:", python_tuple, "\nPython tuple type:", type(python_tuple))

np_array_from_tuple = np.array(python_tuple)
print("\nNumpy array from tuple:", np_array_from_tuple, "\nNumpy array from list type:", type(np_array_from_tuple))


print("\nShape of numpy array\n--------------------")
nums = np.array([1,2,3,4,5])
print("Numpy array:", nums)
print("Shape of numpy array:", nums.shape)

numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
print("\n2D numpy array:\n", numpy_two_dimensional_list)
print("Shape of 2D numpy array:", numpy_two_dimensional_list.shape)

three_by_four_array = np.array([[0, 1, 2, 3], [4,5,6,7], [8,9,10,11]])
print("\n3x4 numpy array:\n", three_by_four_array)
print("\Shape of 3x4 numpy array:", three_by_four_array.shape)


print("\nData type of numpy array\n------------------------")
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print("Int list:", int_lists)
print("\nInt array:", int_array); print("Int array data type:", int_array.dtype)
print("\nFloat array:", float_array); print("Float array data type:", float_array.dtype)


print("\nSize of numpy array\n-------------------")
np_list = [1,2,3,4,5]
np_array_from_list3 = np.array(np_list)

np_2d_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
np_array_from_2d_list = np.array(np_2d_list)

print("List:", np_list); print("Array:", np_array_from_list3)
print("Numpy array size:", np_array_from_list3.size)

print("\n2D list:", np_2d_list); print("2D array:\n", np_array_from_2d_list)
print("2D array size:", np_array_from_2d_list.size)



print("\n\nMathematical Operations using Numpy\n-----------------------------------")

numpy_array_from_list = np.array([1, 2, 3, 4, 5])

print("Addition\n--------")
print('Original array:', numpy_array_from_list)
ten_plus_original = numpy_array_from_list + 10
print("Original array + 10:", ten_plus_original)


print("\nSubtraction\n-----------")
print('Original array:', numpy_array_from_list)
ten_minus_original = numpy_array_from_list - 10
print("Original array - 10:", ten_minus_original)


print("\nMultiplication\n--------------")
print('Original array:', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print("Original array * 10:", ten_times_original)


print("\nDivision\n--------")
print('Original array:', numpy_array_from_list)
original_divide_ten = numpy_array_from_list/10
print("Original array/10:", original_divide_ten)


print("\nModulus\n-------")
print('Original array:', numpy_array_from_list)
original_mod_three = numpy_array_from_list % 3
print("Original array % 3:", original_mod_three)


print("\nFloor Division\n--------------")
print('Original array:', numpy_array_from_list)
ten_fd_original = numpy_array_from_list // 10
print("Original array // 10:", ten_fd_original)


print("\nExponential\n-----------")
print('Original array:', numpy_array_from_list)
two_exp_original = numpy_array_from_list**2
print("Original array ** 2:", two_exp_original)




print("\n\nChecking Data Types\n-------------------")
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print("Int array:", numpy_int_arr, "\nInt array dtype:", numpy_int_arr.dtype)
print("\nFloat array:", numpy_float_arr, "\nFloat array dtype:", numpy_float_arr.dtype)
print("\nBoolean array:", numpy_bool_arr, "\nBoolean array dtype:", numpy_bool_arr.dtype)





print("\n\nConverting Types\n----------------")
int_lst = [1,2,3,4,5]
print("Int list:", int_lst)


print("\nInt to Float\n------------")
int_arr_to_flt = np.array(int_lst, dtype=float)
print("Int array:", np.array(int_lst))
print("Int array to float:", int_arr_to_flt)


print("\nFloat to Int\n------------")
flt_arr_to_int = np.array(int_arr_to_flt, dtype=int)
print("Float array:", int_arr_to_flt)
print("Float array to int:", flt_arr_to_int)


print("\nInt to Bool\n-----------")
int_lst1 = [-3, -2, 0, 1,2,3]
print("Int list:", int_lst)
int_to_bool = np.array(int_lst1, dtype=bool)
print("\nInt array:", np.array(int_lst1))
print("Int array to bool:", int_to_bool)


print("\nInt to String\n-------------")
int_arr_to_str = np.array(int_lst, dtype='<U21') # dtype=str
print("Int array:", np.array(int_lst))
print("Int array to string:", int_arr_to_str)
print("Int array to str type:", int_arr_to_str.dtype)






print("\n\nMulti-dimensional Arrays\n------------------------")
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print("2D array:\n", two_dimension_array)
print("2D array type:", type(two_dimension_array))
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)

print("\nGetting items from numpy array\n------------------------------")

print("Getting row info\n----------------")
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('1st row:', first_row)
print('2nd row:', second_row)
print('3rd row:', third_row)


print("\nGetting column info\n-------------------")
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('1st column:', first_column)
print('2nd column:', second_column)
print('3rd column:', third_column)




print("\n\nSlicing numpy array\n-------------------")
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print("First 2 rows and columns [0:2, 0:2]:\n", first_two_rows_and_columns)




print("\n\nReversing row and column position!\n----------------------------------")
two_dimension_array_reverse = two_dimension_array[::-1,::-1]
print("2D array reversed:\n", two_dimension_array_reverse)




print("\n\nRepresenting missing values\n---------------------------")

two_dimension_array_copy = two_dimension_array.copy()

print("Value substitution\n------------------")
two_dimension_array_copy[1,1] = 55
two_dimension_array_copy[1,2] = 44

print("2D array with substituted values:\n", two_dimension_array_copy)


print("\nZeroes numpy array\n------------------")
np_zeroes = np.zeros((3,3), dtype=int, order='C')
print("Zeroes numpy array:\n", np_zeroes)


print("\nOnes numpy array\n----------------")
np_ones = np.ones((3,3), dtype=int, order='C')
print("Ones numpy array:\n", np_ones)


print("\nReshaping array\n---------------")
first_shape = np.array([(1,2,3), (4,5,6)])
print("Original array:\n", first_shape)

reshaped = first_shape.reshape(3,2)
print("Reshaped array, 3x2:\n", reshaped)


print("\nFlattening array\n----------------")
flattened = reshaped.flatten()
print("Flattened array:", flattened)


print("\nHorizontal append\n-----------------")
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print("List 1:", np_list_one, "\nList 2:", np_list_two)
print("\nList 1 + 2:", np_list_one + np_list_two)
print('Horizontal Append, np.hstack((L1, L2)):', np.hstack((np_list_one, np_list_two)))


print("\nVertical append\n---------------")
print('Horizontal Append, np.vstack((L1, L2)):\n', np.vstack((np_list_one, np_list_two)))


print("\n\nGenerating random numbers\n-------------------------")

print("Random...\n---------")
rndm_float = np.random.random()
print("Float number with np.random.random():", rndm_float)
print("Float number with np.random.random(5):", np.random.random(5))
print("\nnp.random.random(size=[2,3]):\n", np.random.random(size=[2,3]))
print("\nnp.random.rand(2,2):\n", np.random.rand(2,2))
print("\nnp.random.choice(['a', 'e', 'i', 'o', 'u'], size=10):", np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
print("\nnp.random.randint(0, 10, size=[5,3]):\n", np.random.randint(0, 10, size=[5,3]))

print("\nInt number with np.random.randint(0, 11):", np.random.randint(0, 11))
print("Int number with np.random.randint(2,10, size=(3,3)):\n", np.random.randint(2,10, size=(3,3)))

normal_array = np.random.normal(79, 15, 80)
print("\nLarge random array with np.random.normal(79, 15, 80):\n", normal_array)






print("\n\nNumpy and Statistics\n--------------------")
'''
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
plt.show()
'''

four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
print("4x4 ones matrix:\n", four_by_four_matrix)

np.asarray(four_by_four_matrix)[2] = 2
print("\n4x4 matrix with replaced values:\n", four_by_four_matrix)

lst = range(0, 11, 2)
print("\nrange(0, 11 ,2):")
for l in lst:
    print(l)

whole_numbers = np.arange(0, 20, 1)
print("\nnp.arange(0, 20, 1):", whole_numbers)

print("\nOdd numbers, np.arange(1,20,2)", np.arange(1,20,2))
print("Even numbers, np.arange(2,20,2)", np.arange(2,20,2))

print("\nnp.linspace(1.0, 5.0, num=10):\n", np.linspace(1.0, 5.0, num=10)) # Created 10 values from 1 to 5 evenly spaced

print("\nnp.linspace(1.0, 5.0, num=5, endpoint=False):", np.linspace(1.0, 5.0, num=5, endpoint=False)) # Without inclusing last value in interval

print("\nnp.logspace(2, 4.0, num=4)", np.logspace(2, 4.0, num=4)) # Even spaced numbers on a log scale

x = np.array([1,2,3], dtype=np.complex128)
print("\nnp.array([1,2,3], dtype=np.complex128):", x)
print("x.itemsize:", x.itemsize)





print("\n\nNumpy Statistical Functions with Example\n----------------------------------------")

np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis

print("2D array:\n", two_dimension_array_copy)
print("Min:", two_dimension_array_copy.min())
print("Max:", two_dimension_array_copy.max())
print("Mean:", two_dimension_array_copy.mean())
print("SD:", two_dimension_array_copy.std())

# Minimum and Maximum for each column
print('\nColumn with minimum: ', np.amin(two_dimension_array_copy,axis=0)) 
print('Column with maximum: ', np.amax(two_dimension_array_copy,axis=0))

# Min. and Max. for each row
print('\nRow with minimum: ', np.amin(two_dimension_array_copy,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array_copy,axis=1))




print("\nCreate repeating sequences\n--------------------------")
a = [1,2,3]
print("a =", a)

print('\nRepeat whole of a two times, np.tile(a, 2):', np.tile(a, 2))
print('Repeat each element of a two times, np.repeat(a, 2):', np.repeat(a, 2))





print("\n\nHistogram\n---------")
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples

print("Min:", np.min(np_normal_dis))
print("Max:", np.max(np_normal_dis))
print("Mean:", np.mean(np_normal_dis))
print("Median:", np.median(np_normal_dis))
print("Mode:", stats.mode(np_normal_dis))
print("SD:", np.std(np_normal_dis))

import matplotlib.pyplot as plt

plt.hist(np_normal_dis, color='grey', bins=21)
plt.show()





print("\n\nLinear Algebra\n--------------")

print("Dot product\n-----------")
f = np.array([1,2,3])
g = np.array([4,5,3])

print("f =", f)
print("g =", g)
print("Dot product of f and g:", np.dot(f, g))


print("\nMatrix multiplication\n---------------------")
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]

print("h =", h)
print("i =", i)
print("Matrix multiplication using np.matmul(h, i):\n", np.matmul(h, i))


print("\nDeterminant\n-----------")
print("Det. of i, np.linalg.det(i) =", np.linalg.det(i))


print("\nTemp. vs. Pressure\n------------------")
temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5

print("Plotting temp. vs pressure graph...")
plt.plot(temp, pressure)
plt.xlabel("Temperature in °C")
plt.ylabel("Pressure in atm")
plt.title("Temperature vs Pressure")
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()



print("\n\nGaussian Normal Distribution\n----------------------------")
import seaborn as sns

mu = 28
sigma = 15
samples = 100000

print("Plotting Gaussian normal distribution graph...")
x = np.random.normal(mu, sigma, samples)
ax = sns.displot(x)
ax.set(xlabel='x', ylabel='y')
plt.show()