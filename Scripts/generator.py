import random
import math


def read_number(start, end, msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            pass
        else:
            if start <= valor <= end:
                break
    return valor


def generator():
    numbers = read_number(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    mode = read_number(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")

    _list = []

    for i in range(numbers):
        number = random.uniform(0, 101)
        if mode == 1:
            print("{} => {}".format(number, math.ceil(number)))
            number = math.ceil(number)
        elif mode == 2:
            print("{} => {}".format(number, math.floor(number)))
            number = math.floor(number)
        elif mode == 3:
            print("{} => {}".format(number, round(number)))
            number = round(number)
        _list.append(number)

    return _list


generator()
