# This is done as a convention! 'np' is just easier to refer to then 'numpy' all the time.
import numpy as np

# Note here that I use 'one' and 'three'. Your variables in Python can't start with a number, such as '1'.
one_dimensional_matrix = np.array([1, 5, 9])
print(one_dimensional_matrix)

one_dimensional_matrix = one_dimensional_matrix * 3
print(one_dimensional_matrix)

# Three Dimensional Time
three_dimensional_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(three_dimensional_matrix)

three_dimensional_matrix = three_dimensional_matrix * 2
print(three_dimensional_matrix)

print("===")
print("ME CHANGING THE NUMBER 1")
print("===")
three_dimensional_matrix[0][1] = 1
print(three_dimensional_matrix)

print("===")
print("EASIER WAY")
print("===")
an_easier_way = np.array([(1, 0, 0), (0, 1, 0), (0, 0, 1)])
print(an_easier_way)