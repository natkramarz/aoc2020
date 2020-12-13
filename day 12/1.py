directions = ['N', 'E', 'S', 'W']

def change_direction(direction, degrees):
    index = 0
    global main_direction
    for i in range(4):
        if directions[i] == main_direction:
            index = i
            break
    if direction == 'L':
        degrees = -degrees
    main_direction = directions[((index * 90 + degrees) % 360) // 90]


with open('input.txt', 'r') as file:
    lines = file.read().split()
    main_direction = 'E'
    val = 0
    action = ''
    direction_values = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for i in range(len(lines)):
        val = int(lines[i][1:len(lines[i])])
        action = lines[i][0]
        if action == 'F':
            direction_values[main_direction] += val
        elif action == 'L' or action == 'R':
            change_direction(action, val)
        else:
            direction_values[action] += val
    print(abs(direction_values['N'] - direction_values['S']) + abs(direction_values['W'] - direction_values['E']))
