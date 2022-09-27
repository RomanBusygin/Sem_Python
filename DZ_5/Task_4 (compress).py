with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_5\input_data.txt', 'r') as data:
    input_data = data.readline()

compressed_data = ''
count = 1
prev_char = ''

for i in range(1, len(input_data)):
    prev_char = input_data[i - 1]
    if input_data[i] == prev_char:
        count += 1
    else:
        compressed_data += f'{count}{prev_char}'
        count = 1
    if i == len(input_data) - 1:
        compressed_data += f'{count}{prev_char}'

with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_5\output_data.txt', 'w') as out_data:
    out_data.write(compressed_data)