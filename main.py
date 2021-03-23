from Exercise1_2.decisions import maximin, choices_matrix

if __name__ == "__main__":
    print("INITIALIZED")

    maxmin_choice, maxmin_value, maxmin_type = maximin(choices_matrix)
    print(f"VARIANT : {maxmin_choice + 1}",
          f"WITH MIN VALUE : {maxmin_value}",
          f"MAXMIN DECIDING COLUMN : {int(maxmin_type) + 1}")
