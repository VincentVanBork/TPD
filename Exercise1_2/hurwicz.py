import numpy as np
from scikitmcda.dmuu import DMUU
from decisions import choices_matrix


def hurwicz_calc(choices: np.ndarray = choices_matrix, coeff: float = 0.5):
    min_values = np.amin(choices, axis=1)
    max_values = np.amax(choices, axis=1)
    min_indices = np.argmin(choices, axis=1)
    max_indices = np.argmax(choices, axis=1)
    hurwicz_criterions = (coeff * min_values) + ((1 - coeff) * max_values)
    print(f"HURIWCZ CRITERIONS {hurwicz_criterions}")
    return np.argmax(hurwicz_criterions), np.amax(hurwicz_criterions)


if __name__ == "__main__":
    variant, value = hurwicz_calc(choices_matrix, 0.4)
    print(f"CHOICE OF VARIANT {variant + 1} UNDER HURWICZ WITH COEFF {0.4} VALUE OF {value} ")
