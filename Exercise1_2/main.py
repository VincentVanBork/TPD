from .bernoulli_laplace import bernoulli_calc
from .hurwicz import hurwicz_calc
from .maximin import maximin_calc
from .maximax import maximax_calc
from .savage import savage_calc

def main():

    maxmin_choice, maxmin_value, maxmin_type = maximin(choices_matrix)
    print(f"VARIANT : {maxmin_choice + 1}",
          f"WITH MIN VALUE : {maxmin_value}",
          f"MAXMIN DECIDING COLUMN : {int(maxmin_type) + 1}")

if __name__ == "__main__":
    main()