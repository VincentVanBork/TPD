import numpy as np
from typing import Tuple, Any

conditions_num = 3
brakes_num = 3
choices_matrix = np.zeros((brakes_num, conditions_num))
choices_matrix[0][:] = [85.00, 75.00, 95.00]
choices_matrix[1][:] = [85.00, 90.00, 75.5]
choices_matrix[2][:] = [85.00, 65.00, 92.00]
print(choices_matrix)


# WALDS MAXIMIN MODEL
def maximin(choices: np.ndarray) -> Any:
    min_values = np.amin(choices, axis=1)
    min_index = np.argmin(choices, axis=1)
    value_column = np.array(list(zip(min_values, min_index)))
    print(value_column)
    max_index_from_min = np.argmax(value_column[:, 0])
    return max_index_from_min, np.amax(value_column[:, 0]), value_column[max_index_from_min, 1]


maxmin_choice, maxmin_value, maxmin_type = maximin(choices_matrix)
print(f"VARIANT : {maxmin_choice + 1 }",
      f"WITH MIN VALUE : {maxmin_value}",
      f"MAXMIN DECIDING COLUMN : {int(maxmin_type) + 1}")
