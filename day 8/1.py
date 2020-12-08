with open('input.txt', 'r') as file:
    instructions = file.read().split('\n')
    accumulator = 0
    cnt = 0
    was_executed = set()
    while True:
        operation = instructions[cnt].split()
        value = operation[1]
        op = operation[0]
        if cnt in was_executed:
            break
        was_executed.add(cnt)
        if op == "nop":
            cnt += 1
        elif op == "acc":
            cnt += 1
            if value[0] == '-':
                accumulator -= int(value[1:len(value)])
            else:
                accumulator += int(value[1:len(value)])
        elif op == 'jmp':
            if value[0] == '-':
                cnt -= int(value[1:len(value)])
            else:
                cnt += int(value[1:len(value)])

    print(accumulator)