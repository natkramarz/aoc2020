with open('input.txt', 'r') as file:
    instructions = file.read().split('\n')
    accumulator = 0
    cnt = 0
    was_executed = set()
    while True:
        operation = instructions[cnt].split()
        value = int(operation[1])
        op = operation[0]
        if cnt in was_executed:
            print(accumulator)
            break
        was_executed.add(cnt)
        if op == 'jmp':
            cnt += value
        else:
            cnt += 1
            if op == "acc":
                accumulator += value
