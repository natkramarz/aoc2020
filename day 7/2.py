import re

def count_bags(curr_bag):
    bag_num = 0
    if curr_bag in content_of_bags:
        bag_num += 1
        for item in content_of_bags[curr_bag]:
            num = int(content_of_bags[curr_bag][item])
            bag_num += num * count_bags(item)
    else:
        bag_num = 1
    return bag_num


with open('input.txt', 'r') as file:
    lines = file.read().split('\n')
    content_of_bags = dict()
    for i in range(0, len(lines)):
        content = re.split("(?: bags | bags| bag| bag |contain |, |\.)", lines[i])
        for j in range(1, len(content)):
            if len(content[j]) != 0 and content[j] != 'no other':
                bag = content[j][2:len(content[j])]
                if content[0] not in content_of_bags:
                    content_of_bags[content[0]] = dict()
                content_of_bags[content[0]][bag] = content[j][0]
    bag_num = count_bags('shiny gold')
    print(bag_num - 1)
