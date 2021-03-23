import numpy as np
from typing import Tuple, Any
from decisions import choices_matrix

# WALDS MAXIMAX MODEL
def maximax_calc(choices: np.ndarray) -> Any:
    max_values = np.amax(choices, axis=1)
    max_indices = np.argmax(choices, axis=1)
    value_column = np.array(list(zip(max_values, max_indices)))
    print(value_column)
    max_index_from_max = np.argmax(value_column[:, 0])
    return max_index_from_max, np.amax(value_column[:, 0]), value_column[max_index_from_max, 1]


if __name__ == "__main__":
    maxmax_choice, maxmax_value, maxmax_type = maximax_calc(choices_matrix)
    print(f"___ MAXIMAX CALCULATIONS ___"
          f"VARIANT : {maxmax_choice + 1}",
          f"WITH MAX VALUE : {maxmax_value}",
          f"MAXIMAX DECIDING COLUMN : {int(maxmax_type) + 1}")
