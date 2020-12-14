import math
with open('input.txt', 'r') as file:
    t = int(file.readline())
    buses = file.readline().split(',')
    buses_timestamps = dict()
    for i in range(len(buses)):
        if buses[i] != 'x':
            buses[i] = int(buses[i])
            buses_timestamps[i] = math.ceil(t / buses[i]) * buses[i]
    min = -1
    index = 0
    for item in buses_timestamps.items():
        if item[1] < min or min == -1:
            min = item[1]
            index = item[0]
    print(buses[index] * (min - t))
