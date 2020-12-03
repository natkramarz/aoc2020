with open('input.txt', 'r') as file:
    passwords = file.read().split('\n')
    ctn = 0
    for i in range(0, len(passwords)):
        parts = passwords[i].split(': ', 1)
        char = parts[0][-1]
        nums = parts[0].partition('-')
        num1 = nums[0]
        num2 = nums[2].partition(' ')
        num2 = num2[0]
        char_ctn = 0
        for j in range(0, len(parts[1])):
            if parts[1][j] == char:
                char_ctn += 1
        if int(num2) >= char_ctn >= int(num1):
            ctn += 1
print(ctn)
