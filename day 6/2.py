with open('input.txt', 'r') as file:
    groups = file.read().split('\n\n')
    num_answers = 0

    for i in range(len(groups)):
        group = groups[i].split('\n')
        answers = {}
        for j in range(len(group)):
            for k in range(len(group[j])):
                if group[j][k] in answers:
                    answers[group[j][k]] += 1
                else:
                    answers[group[j][k]] = 1

        for item in answers.items():
            if item[1] == len(group) and len(group) >= 2:
                num_answers += 1
            elif len(group) == 1:
                num_answers += 1

    print(num_answers)
