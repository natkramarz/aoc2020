def find_two(nums_list, numbers_dict):
    n = len(nums)
    for i in range(0, n - 1):
        second_number = 2020 - nums_list[i]
        if second_number in numbers_dict:
            return nums_list[i] * second_number

def find_three(nums_list, numbers_dict):
    n = len(nums)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            third_num = 2020 - nums_list[i] - nums_list[j]
            if third_num in numbers_dict:
                return nums[i] * nums_list[j] * third_num


nums_dict = {}
file = open('input.txt', 'r')
nums = file.readlines()
file.close()
for i in range(0, len(nums)):
    nums[i] = int(nums[i])
    nums_dict[nums[i]] = nums[i]
print(find_two(nums, nums_dict))
print(find_three(nums, nums_dict))

