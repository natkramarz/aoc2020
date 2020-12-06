def find_row(seat_str):
    lower = 0
    upper = 127
    for i in range(7):
        mid = (lower + upper) // 2
        if seat_str[i] == 'B':
            lower = mid
        elif seat_str[i] == 'F':
            upper = mid
    if seat_str[6] == 'B':
        mid += 1
    return mid

def find_col(seat_str):
    col_low = 0
    col_upper = 7
    for i in range(7, 10):
        col_mid = (col_low + col_upper) // 2
        if seat_str[i] == 'R':
            col_low = col_mid
        elif seat_str[i] == 'L':
            col_upper = col_mid

    if seat_str[9] == 'R':
        col_mid += 1

    return col_mid


with open('input.txt', 'r') as file:
    boarding_passes = file.read().split('\n')
    seats = [[] for i in range(128)]
    for i in range(0, len(boarding_passes)):
        curr_row = find_row(boarding_passes[i])
        seats[curr_row].append(i)
    row = 0
    column = 0
    taken_seats = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(128):
        if len(seats[i]) == 7:
            row = i
            for j in range(7):
                taken_seats[find_col(boarding_passes[seats[i][j]])] = 1
            break
    for i in range(8):
        if taken_seats[i] == 0:
            column = i
            break
    print(row * 8 + column)