from cmath import pi


def precision_number_pi(number: float, digit: int) -> float:
    number_string = str(number)
    new_number_string = ""
    for i in range(2 + digit):
        new_number_string += number_string[i]
    return float(new_number_string)

dig = int(input('Сколько знаков Пи надо сохранить? '))
print(precision_number_pi(pi, dig))