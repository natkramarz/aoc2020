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
                    occupied_cnt = 0
                    k = i
                    l = j
                    while k - 1 >= 0 and l - 1 >= 0:
                        if lines[k - 1][l - 1] == 'L':
                            break
                        if lines[k - 1][l - 1] == '#':
                            occupied_cnt += 1
                            break
                        k -= 1
                        l -= 1
                    k = i
                    l = j
                    while k - 1 >= 0 and l + 1 < len(lines[i]):
                        if lines[k - 1][l + 1] == 'L':
                            break
                        if lines[k - 1][l + 1] == '#':
                            occupied_cnt += 1
                            break
                        k -= 1
                        l += 1
                    k = i
                    l = j
                    while k + 1 < len(lines) and l - 1 >= 0:
                        if lines[k + 1][l - 1] == 'L':
                            break
                        if lines[k + 1][l - 1] == '#':
                            occupied_cnt += 1
                            break
                        k += 1
                        l -= 1
                    k = i
                    l = j
                    while k + 1 < len(lines) and l + 1 < len(lines[i]):
                        if lines[k + 1][l + 1] == 'L':
                            break
                        if lines[k + 1][l + 1] == '#':
                            occupied_cnt += 1
                            break
                        k += 1
                        l += 1
                    k = i
                    l = j
                    while l - 1 >= 0:
                        if lines[i][l - 1] == 'L':
                            break
                        if lines[i][l - 1] == '#':
                            occupied_cnt += 1
                            break
                        l -= 1
                    k = i
                    l = j
                    while l + 1 < len(lines[i]):
                        if lines[i][l + 1] == 'L':
                            break
                        if lines[i][l + 1] == '#':
                            occupied_cnt += 1
                            break
                        l += 1
                    k = i
                    l = j
                    while k + 1 < len(lines):
                        if lines[k + 1][j] == 'L':
                            break
                        if lines[k + 1][j] == '#':
                            occupied_cnt += 1
                            break
                        k += 1
                    k = i
                    l = j
                    while k - 1 >= 0:
                        if lines[k - 1][j] == 'L':
                            break
                        if lines[k - 1][j] == '#':
                            occupied_cnt += 1
                            break
                        k -= 1

                    if lines[i][j] == 'L' and occupied_cnt == 0:
                        helper_list[i][j] = '#'
                        was_changed = True
                    if lines[i][j] == '#' and occupied_cnt >= 5:
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
