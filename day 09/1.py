def check_sum(num, array, length) -> bool:
    for j in range(length):
        for k in range(j + 1, length):
            if num == array[j] + array[k]:
                return True
    return False


with open('input.txt', 'r') as file:
    lines = file.read().split()
    pre_length = 25
    preamble = []
    for i in range(pre_length):
        preamble.append(int(lines[i]))
    pre_cnt = 0
    for i in range(pre_length, len(lines)):
        curr_num = int(lines[i])
        if check_sum(curr_num, preamble, pre_length):
            preamble[pre_cnt] = curr_num
            if pre_cnt < pre_length - 1:
                pre_cnt += 1
            else:
                pre_cnt = 0
        else:
            print(curr_num)
            break
