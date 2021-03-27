import numpy as np
from decisions import choices_matrix


def savage_cals(choices: np.ndarray):
    max_from_row = np.vstack(np.amax(choices, axis=1))
    print(max_from_row)
    relative_losses = max_from_row - choices
    print(relative_losses)
    losses_max = np.amax(relative_losses, axis=1)
    print(losses_max)
    return np.argmin(losses_max), np.amin(losses_max)


if __name__ == "__main__":
    variant, loss_value = savage_cals(choices_matrix)
    print("VARIANT ", variant + 1, "MINIMAL LOSSES", loss_value)
