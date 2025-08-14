

def find_min(nums):
    left, right = 0, len(nums) - 1  # assigning 0th index to left and last index to right

    while left < right:  # breaks when left and right are equal
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:  # if mid is greater that right the min lies in right half
            left = mid + 1
        elif nums[mid] <= nums[right]:  # if mid is smaller than or equal to right the min lies at mid or in left half
            right = mid

    return nums[left]  # left == right, either nums[left] or nums[right]

