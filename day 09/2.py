def check_sum_of_2(num, array, length) -> bool:
    for j in range(length):
        for k in range(j + 1, length):
            if num == array[j] + array[k]:
                return True
    return False

def check_sum_of_many(num, length):
    sum = 0
    for j in range(length):
        sum = int(lines[j])
        array = []
        array.append(sum)
        for k in range(j + 1, length):
            if sum + int(lines[k]) == num:
                array.sort()
                return array[0] + array[len(array) - 1]
            elif sum + int(lines[k]) > num:
                break
            else:
                sum += int(lines[k])
                array.append(int(lines[k]))


with open('input.txt', 'r') as file:
    lines = file.read().split()
    pre_length = 25
    preamble = []
    for i in range(pre_length):
        preamble.append(int(lines[i]))
    pre_cnt = 0
    for i in range(pre_length, len(lines)):
        curr_num = int(lines[i])
        if check_sum_of_2(curr_num, preamble, pre_length):
            preamble[pre_cnt] = curr_num
            if pre_cnt < pre_length - 1:
                pre_cnt += 1
            else:
                pre_cnt = 0
        else:
            print(check_sum_of_many(curr_num, i))
            break

