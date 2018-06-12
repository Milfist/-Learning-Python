error_type_not_valid = "Error: Tipo de dato no válido"
error_zero_division = "Error: No es posible dividir entre cero"


def sum_(num_1, num_2):
    try:
        return num_1 + num_2
    except TypeError:
        print(error_type_not_valid)


def subtraction(num_1, num_2):
    try:
        return num_1 - num_2
    except TypeError:
        print(error_type_not_valid)


def multiply(num_1, num_2):
    try:
        return num_1 * num_2
    except TypeError:
        print(error_type_not_valid)


def partition(num_1, num_2):
    try:
        return num_1 / num_2
    except TypeError:
        print(error_type_not_valid)
    except ZeroDivisionError:
        print(error_zero_division)
