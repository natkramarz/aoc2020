def check_highest_row(array, ptr) -> list:
    back = []
    front = []
    for i in range(0, len(array)):
        if array[i][ptr] == 'B':
            back.append(array[i])
        elif array[i][ptr] == 'F':
            front.append(array[i])
    if len(back) != 0:
        return back
    return front

def check_highest_seat(array, ptr):
    upper = []
    lower = []
    for i in range(0, len(array)):
        if array[i][ptr] == 'R':
            upper.append(array[i])
        elif array[i][ptr] == 'L':
            lower.append(array[i])
    if len(upper) != 0:
        return upper
    return lower

def convert_binary(seat_str):
    lower = 0
    upper = 127
    for i in range(0, 7):
        mid = (lower + upper) // 2
        if seat_str[i] == 'B':
            lower = mid
        elif seat_str[i] == 'F':
            upper = mid
    col_low = 0
    col_upper = 7
    for i in range(7, 10):
        col_mid = (col_low + col_upper) // 2
        if seat_str[i] == 'R':
            col_low = col_mid
        elif seat_str[i] == 'L':
            col_upper = col_mid
    return 8 * mid + col_mid


with open('input.txt', 'r') as file:
    boarding_passes = file.read().split('\n')
    ptr = 0
    for i in range(0, 7):
        boarding_passes = check_highest_row(boarding_passes, ptr)
        ptr += 1
    for i in range(0, 3):
        boarding_passes = check_highest_seat(boarding_passes, ptr)
        ptr += 1
    print(convert_binary(boarding_passes[0]))
