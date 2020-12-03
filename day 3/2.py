with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    steps_num = [1, 3, 5, 7]
    curr_steps = [0, 0, 0, 0]
    tree_cnt = [0, 0, 0, 0]
    for line_ctn in range(0, len(lines)):
        for i in range(0, len(curr_steps)):
            if curr_steps[i] >= len(lines[line_ctn]):
                curr_steps[i] = curr_steps[i] - len(lines[line_ctn])
            if curr_steps[i] < len(lines[line_ctn]) and lines[line_ctn][curr_steps[i]] == '#':
                tree_cnt[i] += 1
            curr_steps[i] += steps_num[i]

    j = 0
    right_step = 0
    tree_cnt2 = 0
    while j < len(lines):
        if right_step >= len(lines[j]):
            right_step = right_step - len(lines[j])
        if right_step < len(lines[j]) and lines[j][right_step] == '#':
            tree_cnt2 += 1
        right_step += 1
        j += 2
    print(tree_cnt2 * tree_cnt[0] * tree_cnt[1] * tree_cnt[2] * tree_cnt[3])
