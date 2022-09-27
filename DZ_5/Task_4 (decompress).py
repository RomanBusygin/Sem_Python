with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_5\input_data.txt', 'r') as data:
    input_data = data.readline()

decompressed_data = ''
count = ''

for i in range(len(input_data)):
    if input_data[i].isdigit():
        count += input_data[i]
    else:
        decompressed_data += int(count) * input_data[i]
        count = ''

with open(r'C:\Users\Roman\Desktop\GEEK block 2\Python\DZ\DZ_5\output_data.txt', 'w') as out_data:
    out_data.write(decompressed_data)