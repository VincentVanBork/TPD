from bernoulli_laplace import bernoulli_calc
from hurwicz import hurwicz_calc
from maximin import maximin_calc
from maximax import maximax_calc
from savage import savage_calc
from numpy import genfromtxt
import argparse, sys
from sys import argv


def get_action(name):
    all_actions = {"Hurwicz": hurwicz_calc,
                   "Laplace": bernoulli_calc,
                   "MAXiMAX": maximax_calc,
                   "MAXiMIN": maximin_calc,
                   "Savage": savage_calc
                   }
    return all_actions[name]


def main(*args, **kwargs):
    print(args)
    array_data = genfromtxt(args[0].file, delimiter=',')
    action = args[0].action
    print("INITIALIZED")
    # print(array_data)
    # print(action, args[0].p, args[0].c)
    if action == "Hurwicz":
        variant, value = get_action(action)(array_data, float(args[0].c))
        print("VARIANT",
              variant + 1,
              "with value", value,
              "at coeff for negative", args[0].c)

    elif action == "Laplace":
        probability = genfromtxt(args[0].p, delimiter=',')
        variant, value = get_action(action)(array_data, probability)
        print("BEST VARIANT", variant + 1,
              "WITH VALUE", value)

    elif action == "MAXiMAX" or action == "MAXiMIN":
        variant, value, deciding = get_action(action)(array_data)
        print(f" VARIANT : {variant + 1}",
              f"WITH VALUE : {value}",
              f" DECIDING COLUMN : {int(deciding) + 1}")
    else:
        variant, value = get_action(action)(array_data)
        print("VARIANT ", variant + 1, "MINIMAL LOSSES", value)


if __name__ == "__main__":
    action_choices = ['Hurwicz', 'Laplace', 'MAXiMAX', 'MAXiMIN', 'Savage']
    parser = argparse.ArgumentParser()
    parser.add_argument('--action',
                        choices=action_choices,
                        default='MAXiMIN',
                        help='Hurwicz, Laplace, MAXiMAX, MAXiMIN, Savage decision criteria types')
    parser.add_argument('-c', required=(action_choices[0] in argv))
    parser.add_argument('--file',
                        help='name of the file  (csv , only implemented) with the array')
    parser.add_argument('-p',
                        required=(action_choices[1] in argv),
                        help="PROBABILITY for laplace action, space separated")

    arguments = parser.parse_args()

    main(arguments)
