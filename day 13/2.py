from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


with open('input.txt', 'r') as file:
    num = int(file.readline())
    buses = file.readline().split(',')
    buses_nums = []
    buses_timestamps = []
    for i in range(len(buses)):
        if buses[i] != 'x':
            buses_nums.append(int(buses[i]))
            buses_timestamps.append(i)
    print(buses_nums)
    print(buses_timestamps)
    print(abs(chinese_remainder(buses_nums, buses_timestamps) - reduce(lambda x, y: x*y, buses_nums)))
