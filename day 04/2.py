eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def check_data(person_data) -> bool:
    for j in range(0, len(data)):
        info = person_data[j].split(':')
        if info[0] == 'byr' and not (1920 <= int(info[1]) <= 2002):
            return False
        elif info[0] == 'iyr' and not (2010 <= int(info[1]) <= 2020):
            return False
        elif info[0] == 'eyr' and not (2020 <= int(info[1]) <= 2030):
            return False
        elif info[0] == 'hgt':
            if 'in' in info[1]:
                if not (59 <= int(info[1][0:-2]) <= 76):
                    return False
            elif 'cm' in info[1]:
                if not (150 <= int(info[1][0:-2]) <= 193):
                    return False
            else:
                return False
        elif info[0] == 'hcl':
            if not(info[1][0] == '#'):
                return False
            substr = info[1][1:len(info[1])]
            if not (len(substr) == 6):
                return False
            for char in substr:
                if not(char.isdigit() or char.islower() or char.isupper()):
                    return False
        elif info[0] == 'ecl':
            if not(info[1] in eye_colors):
                return False
        elif info[0] == 'pid':
            if not (len(info[1]) == 9):
                return False

    return True


with open('input.txt', 'r') as file:
    lines = file.read().split('\n\n')
    cnt = 0
    for i in range(0, len(lines)):
        data = lines[i].split()
        if len(data) == 8:
            if check_data(data):
                cnt += 1
        elif len(data) == 7:
            fields = set()
            for j in range(0, len(data)):
                fields.add(data[j][0:3])
            if not ("cid" in fields):
                if check_data(data):
                    cnt += 1
    print(cnt)
