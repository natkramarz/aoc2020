import functools

@functools.lru_cache(None)
def check_sub_array(start):
    arrangement_cnt = 0
    if start == len(lines):
        return 1
    for j in range(start, len(lines)):
        if j + 2 < length and lines[j + 2] - lines[j] < 4:
            arrangement_cnt += 1
            arrangement_cnt += check_sub_array(j + 2)
        if j + 3 < length and lines[j + 3] - lines[j] < 4:
            arrangement_cnt += 1
            arrangement_cnt += check_sub_array(j + 3)
    return arrangement_cnt


with open('input.txt', 'r') as file:
    lines = file.read().split()
    lines = [int(i) for i in lines]
    lines.sort()
    lines.insert(0, 0)
    length = len(lines)
    arrangement_cnt = check_sub_array(0) + 1
    print(arrangement_cnt)

