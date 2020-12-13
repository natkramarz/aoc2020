with open('input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    num_answers = 0
    for i in range(len(groups)):
        group = groups[i].split('\n')
        answers = set()
        for j in range(len(group)):
            for k in range(len(group[j])):
                answers.add(group[j][k])
        num_answers += len(answers)
    print(num_answers)
