import numpy as np
from typing import Any
from decisions import choices_matrix

# WALDS MAXIMIN MODEL
def maximin_calc(choices: np.ndarray) -> Any:
    min_values = np.amin(choices, axis=1)
    min_index = np.argmin(choices, axis=1)
    value_column = np.array(list(zip(min_values, min_index)))
    print(value_column)
    max_index_from_min = np.argmax(value_column[:, 0])
    return max_index_from_min, np.amax(value_column[:, 0]), value_column[max_index_from_min, 1]


if __name__ == "__main__":
    maxmin_choice, maxmin_value, maxmin_type = maximin_calc(choices_matrix)
    print(f"___ MAXIMIN CALCULATIONS ___"
          f" VARIANT : {maxmin_choice + 1}",
          f"WITH MIN VALUE : {maxmin_value}",
          f"MAXMIN DECIDING COLUMN : {int(maxmin_type) + 1}")
