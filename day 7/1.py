import re
def find_bags(curr_bag):
    if curr_bag in in_which_bags:
        for item in in_which_bags[curr_bag]:
            options.add(item)
            find_bags(item)

with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    in_which_bags = dict()
    for i in range(0, len(lines)):
        content = re.split("(?: bags | bags| bag| bag |contain |, |\.)", lines[i])
        for j in range(1, len(content)):
            if len(content[j]) != 0 and content[j] != 'no other':
                bag = content[j][2:len(content[j])]
                if bag not in in_which_bags:
                    in_which_bags[bag] = set()
                in_which_bags[bag].add(content[0])
    options = set()
    find_bags('shiny gold')
    print(len(options))