def simple_multipliers(n: int) -> list:
    s_m_list = []
    for i in range(2, n + 1):
        while n % i == 0:
            n /= i
            s_m_list.append(i)
    return(s_m_list)
    

number = int(input('Введите натуральное число: '))
print(f'Простые множители числа {number} - {simple_multipliers(number)}')