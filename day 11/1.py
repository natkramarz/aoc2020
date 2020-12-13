with open('input.txt', 'r') as file:
    lines = file.read().split()
    for i in range(len(lines)):
        lines[i] = [char for char in lines[i]]
    was_changed = True
    helper_list = []
    while was_changed:
        was_changed = False
        helper_list = []
        for i in range(len(lines)):
            helper_list.append([])
            helper_list[i] += lines[i]
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] != '.':
                    empty = True
                    occupied_cnt = 0
                    if lines[i][j] == '#':
                        empty = False
                    if i - 1 >= 0:
                        if j - 1 >= 0 and lines[i - 1][j - 1] == '#':
                            occupied_cnt += 1
                        if j + 1 < len(lines[i]) and lines[i - 1][j + 1] == '#':
                            occupied_cnt += 1
                        if lines[i - 1][j] == '#':
                            occupied_cnt += 1
                    if j - 1 >= 0 and lines[i][j - 1] == '#':
                        occupied_cnt += 1
                    if j + 1 < len(lines[i]) and lines[i][j + 1] == '#':
                        occupied_cnt += 1
                    if i + 1 < len(lines):
                        if j - 1 >= 0 and lines[i + 1][j - 1] == '#':
                            occupied_cnt += 1
                        if j + 1 < len(lines[i]) and lines[i + 1][j + 1] == '#':
                            occupied_cnt += 1
                        if lines[i + 1][j] == '#':
                            occupied_cnt += 1
                    if empty and occupied_cnt == 0:
                        helper_list[i][j] = '#'
                        was_changed = True
                    if not empty and occupied_cnt >= 4:
                        helper_list[i][j] = 'L'
                        was_changed = True
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                lines[i][j] = helper_list[i][j]

    seat_cnt = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                seat_cnt += 1
    print(seat_cnt)
