def sum_polinoms(poli_1: str, poli_2: str) -> str:
    members_1 = poli_1.split(' + ')
    members_2 = poli_2.split(' + ')
    indexes_1 = []
    indexes_2 = []
    new_polinom = ""

    for i in range(len(members_1)):
        indexes_1.append(members_1[i].split('x^'))
    for i in range(len(members_2)):
        indexes_2.append(members_2[i].split('x^'))
    
    max_polinom = indexes_1
    min_polinom = indexes_2
    if len(min_polinom) > len(max_polinom):
        max_polinom = indexes_2
        min_polinom = indexes_1
    
    for m in range(len(max_polinom) - 1):
        match = 0
        for n in range(len(min_polinom) - 1):
            if max_polinom[m][1] == min_polinom[n][1]:
                new_polinom += f'{int(max_polinom[m][0]) + int(min_polinom[n][0])}x^{max_polinom[m][1]} + '
                match = 1
        if match == 0:
            new_polinom += f'{max_polinom[m][0]}x^{max_polinom[m][1]} + '
    
    if len(max_polinom[-1]) and len(min_polinom[-1]) == 1:
        new_polinom += f'{int(max_polinom[-1][0]) + int(min_polinom[-1][0])}'
    
    return new_polinom


with open('file.txt', 'r') as file:
    polinom_1 = file.readline()
with open('file_2.txt', 'r') as file_2:
    polinom_2 = file_2.readline()
with open('sum_file.txt', 'w') as sum_file:
    sum_file.write(sum_polinoms(polinom_1, polinom_2))