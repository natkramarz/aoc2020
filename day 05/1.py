def convert_to_binary(str, start, end, char):
    converted_number = 0
    for i in range(start, end):
        converted_number = converted_number << 1
        if str[i] == char:
            converted_number += 1
    return converted_number


with open('input.txt', 'r') as file:
    boarding_passes = file.read().split('\n')
    highest = 0
    for i in range(len(boarding_passes)):
        row = convert_to_binary(boarding_passes[i], 0, 7, 'B')
        col = convert_to_binary(boarding_passes[i], 7, 10, 'R')
        if (row * 8 + col) > highest:
            highest = row * 8 + col
    print(highest)