with open('input.txt', 'r') as file:
    passwords = file.read().split('\n')
    ctn = 0
    for i in range(0, len(passwords)):
        parts = passwords[i].split(': ', 1)
        char = parts[0][-1]
        nums = parts[0].partition('-')
        num1 = int(nums[0]) - 1
        num2 = nums[2].partition(' ')
        num2 = int(num2[0]) - 1
        if num1 < len(parts[1]) and num2 < len(parts[1]):
            if (parts[1][num2] == char and parts[1][num1] != char) or (parts[1][num2] != char and parts[1][num1] == char):
                    ctn += 1
    print(ctn)