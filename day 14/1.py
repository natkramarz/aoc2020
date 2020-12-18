with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    mask = ''
    mem = dict()
    sum = 0
    for i in range(len(lines)):
        if lines[i][0:4] == 'mask':
            mask = lines[i][7:len(lines[i])][::-1]
        else:
            start = '['
            end = ']'
            mem_num = int(lines[i][lines[i].index(start)+len(end):lines[i].index(end)])
            val = int(lines[i].rsplit(' ', 1)[1])
            for j in range(len(mask)):
                if mask[j] != 'X':
                    if mask[j] == '0':
                        val = val & (~(1 << j))
                    else:
                        val = val | (1 << j)
            mem[mem_num] = val
    for key, val in mem.items():
        sum += val
    print(sum)
