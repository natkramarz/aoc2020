coordinates = [(1, 0, 1, 1), (1, 1, -1, 0), (-1, 0, -1, 1), (-1, 1, 1, 0)]

def change_direction(direction, degrees):
    global waypoint
    if direction == 'L':
        degrees = -degrees
    degrees = (degrees % 360) // 90
    x = coordinates[degrees][0] * waypoint[coordinates[degrees][1]]
    y = coordinates[degrees][2] * waypoint[coordinates[degrees][3]]
    waypoint[0] = x
    waypoint[1] = y


with open('input.txt', 'r') as file:
    lines = file.read().split()
    waypoint = [10, 1]
    val = 0
    action = ''
    curr_point = [0, 0]
    for i in range(len(lines)):
        val = int(lines[i][1:len(lines[i])])
        action = lines[i][0]
        if action == 'F':
            curr_point[0] += waypoint[0] * val
            curr_point[1] += waypoint[1] * val
        elif action == 'L' or action == 'R':
            change_direction(action, val)
        else:
            if action == 'S' or action == 'W':
                val = -val
            if action == 'S' or action == 'N':
                waypoint[1] += val
            else:
                waypoint[0] += val
    print(abs(curr_point[0]) + abs(curr_point[1]))
