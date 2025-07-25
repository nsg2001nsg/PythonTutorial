import copy
import random

nums = random.sample(range(-50, 151), random.randint(3, 11))

# print(f"Unsorted List: {nums}")


def insertion_sort(nums):
    size = len(nums)
    count = 0
    for i in range(1, size):
        for j in range(i-1, -1, -1):
            count += 1
            if nums[j] <= nums[i]:
                break
            elif nums[j] > nums[i]:
                nums[j], nums[i] = nums[i], nums[j]  # swapping (incprrect)
                i = j

    print(count)
    return nums


def insertion_sort_opt(nums):
    size = len(nums)
    count = 0
    for i in range(1, size):
        value = nums[i]  # 1
        j = i - 1  # 2 1 0 -1
        while j >= 0 and value < nums[j]:
            count += 1
            nums[j + 1] = nums[j]  # assigning / shifting
            j -= 1
        nums[j + 1] = value

    print(count)
    return nums


print(f"original list: {nums}")
print(f"sorted list: {insertion_sort(copy.copy(nums))}")
print(f"original list: {nums}")
print(f"sorted list: {insertion_sort_opt(copy.copy(nums))}")



