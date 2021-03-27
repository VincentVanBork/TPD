import numpy as np

conditions_num = 3
brakes_num = 3
weight_hurwicz = 0.5
choices_matrix = np.zeros((brakes_num, conditions_num))
choices_matrix[0][:] = [85.00, 75.00, 95.00]
choices_matrix[1][:] = [85.00, 90.00, 75.5]
choices_matrix[2][:] = [85.00, 65.00, 92.00]
probability_even = np.array([1 / 3, 1 / 3, 1 / 3])
probability_different = np.array([1 / 8, 5 / 8, 2 / 8])
print(choices_matrix)
