def convert_to_binary(str, start, end, char):
    converted_number = 0
    for i in range(start, end):
        converted_number = converted_number << 1
        if str[i] == char:
            converted_number += 1
    return converted_number


with open('input.txt', 'r') as file:
    boarding_passes = file.read().split('\n')
    seats = [[] for i in range(128)]
    for i in range(0, len(boarding_passes)):
        curr_row = convert_to_binary(boarding_passes[i], 0, 7, 'B')
        seats[curr_row].append(i)
    row = 0
    column = 0
    taken_seats = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(128):
        if len(seats[i]) == 7:
            row = i
            for j in range(7):
                taken_seats[convert_to_binary(boarding_passes[seats[i][j]], 7, 10, 'R')] = 1
            break
    for i in range(8):
        if taken_seats[i] == 0:
            column = i
            break
    print(row * 8 + column)