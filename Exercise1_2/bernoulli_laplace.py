from typing import Optional

import numpy as np
from decisions import choices_matrix, probability_even, probability_different


def bernoulli_calc(choices: np.ndarray = choices_matrix,
                   probability_variants: Optional[np.ndarray] = None):
    if probability_variants is not None:
        probability_values = probability_variants * choices
        variants = probability_values.sum(axis=1)
        # print("p values", probability_values)
        # print("final ", variants)
    else:
        num_rows, num_cols = choices.shape
        sum_of_types = choices.sum(axis=1)
        variants = (1 / num_cols) * sum_of_types
        # print("sum", variants)
    print("BEST VARIANT", np.argmax(variants) + 1,
          "WITH VALUE", np.amax(variants))
    return np.argmax(variants), np.amax(variants)


if __name__ == "__main__":
    bernoulli_calc(choices_matrix)
    bernoulli_calc(choices_matrix, probability_different)
