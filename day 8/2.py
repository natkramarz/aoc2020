def check_if_stops():
    accumulator = 0
    cnt = 0
    was_executed = set()
    while True:
        if cnt >= len(instructions):
            return accumulator
        operation = instructions[cnt].split()
        value = int(operation[1])
        op = operation[0]
        if cnt in was_executed:
            return None
        was_executed.add(cnt)
        if op == "nop":
            cnt += 1
        elif op == "acc":
            cnt += 1
            accumulator += value
        elif op == 'jmp':
           cnt += value


with open('input.txt', 'r') as file:
    instructions = file.read().split('\n')
    i = 0
    while i < len(instructions):
        op = instructions[i].split()[0]
        while op == 'acc':
            i += 1
            if i < len(instructions):
                op = instructions[i].split()[0]
        else:
            value = int(instructions[i].split()[1])
            if op == 'nop' and value != 0:
                instructions[i] = instructions[i].replace('nop', 'jmp')
                acc = check_if_stops()
                if acc is not None:
                    print(acc)
                    break
                instructions[i] = instructions[i].replace('jmp', 'nop')
            elif op == 'jmp':
                instructions[i] = instructions[i].replace('jmp', 'nop')
                acc = check_if_stops()
                if acc is not None:
                    print(acc)
                    break
                instructions[i] = instructions[i].replace('nop', 'jmp')
            i += 1