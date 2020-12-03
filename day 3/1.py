with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    right_step = 0
    tree_cnt = 0
    lines_cnt = 0
    for i in range(0, len(lines)):
        if right_step >= len(lines[i]):
            right_step = right_step - len(lines[i])
        if right_step < len(lines[i]) and lines[i][right_step] == '#':
            tree_cnt += 1
        right_step += 3
    print(tree_cnt)
