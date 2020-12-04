with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')
    cnt = 0
    for i in range(0, len(lines)):
        data = lines[i].split()
        if len(data) == 8:
            cnt += 1
        elif len(data) == 7:
            fields = set()
            for j in range(0, len(data)):
                fields.add(data[j][0:3])
            if not ("cid" in fields):
                cnt += 1
    print(cnt)
