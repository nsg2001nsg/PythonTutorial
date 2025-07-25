import copy
import random

nums = random.sample(range(-50, 100), random.randint(3, 11))

print(f"Unsorted List: {nums}")


def selection_sort(num):
    size = len(num)
    count = 0
    for o in range(size-1):
        min_index = o
        for i in range(o + 1, size):
            count += 1
            if num[i] < num[min_index]:
                min_index = i
        num[o], num[min_index] = num[min_index], num[o]
    print(count)
    return num


print(f"Original List: {nums}")
print(f"Sorted List: {selection_sort(copy.deepcopy(nums))}")


# nums1 = [1, 2, 3, 4, 5]
# nums1 = ["1", "2", "3", "4", "5"]
# nums1 = ["one", "two", "three", "four", "five"]
# nums1 = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

# nums2 = nums1  # referencing
# nums2 = copy.copy(nums1)  # copy shallow
# nums2 = copy.deepcopy(nums1)  # copy deep
# print(f"nums1 List: {nums1}")
# print(f"nums1 id: {id(nums1)}")
# print(f"nums1[0] id: {id(nums1[0])}")
# print(f"nums1[1] id: {id(nums1[1])}")
# print(f"nums2 List: {nums2}")
# print(f"nums2 id: {id(nums2)}")
# print(f"nums2[0] id: {id(nums2[0])}")
# print(f"nums2[1] id: {id(nums2[1])}")
