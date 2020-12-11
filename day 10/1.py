with open('input.txt', 'r') as file:
    lines = file.read().split()
    lines = [int(i) for i in lines]
    lines.sort()
    lines.append(lines[len(lines) - 1] + 3)
    curr_adapter = 0
    length = len(lines)
    jolt1 = 0
    jolt3 = 0
    for i in range(length):
        diff = lines[i] - curr_adapter
        if diff == 1:
            jolt1 += 1
        elif diff == 3:
            jolt3 += 1
        curr_adapter = lines[i]
    print(jolt1 * jolt3)


