import numpy as np

# arr = np.array([x for x in range(1, 11)])
# print(arr.shape)
# print(arr.size)
# print(arr.dtype)
#
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.reshape(arr, (10, 1)))  # used for redefining dimensions of array without changing the data itself
# print(np.reshape(arr, (5, -1)))  # the tuple has 2 args rows and columns... one of which could be -1 and numpy handles the other one.
#
# new_arr = arr ** 2 + 3
# print(new_arr)
#
# # new_arr = np.array([x * 2 for x in arr[:] if x > 20])
#
# print(arr > 20)  # returns a list of boolean values applied on each element
# # when this boolean list is passed into slicing it only selects where element corresponds with 1
#
# new_arr = new_arr[new_arr > 20]
# new_arr = new_arr * 2
# print(new_arr)

# arr = np.array([2, 5, 8, 10, 15])
# arr = (arr ** 2 + 5) // 2
# print(arr)
#
# arr = np.array([1, 2, 3, 4, 5])
# # arr = arr ** 2 + 10  # squared an added 10
#
# arr = np.array([x * 2 for x in arr[:]])  # using np.where we can simulate traversing through each element and acting on conditions
# print(arr)
# arr1 = np.arange(1, 11)
# arr1 = (arr1 * 3) - (arr1 ** 2)
#
# arr2 = np.array([1, 2, 3, 4, 5])
# print(1/arr2)
#
# arr = np.array([2, 7, 10, 4, 15, 3, 23])
# # arr = arr[(arr > 5) & (arr % 2)]
# # arr = arr[arr % 3 != 0]
#
# np.where(condition) – gives indices where condition is True.
# # arr = np.where(arr > 10, "Big", "Small")
# # arr = np.where(arr % 3 == 0, "Fizz", np.where(arr % 5 == 0, "Buzz", "other"))
#
# # arr = np.where((arr % 3 == 0) & (arr % 5 == 0), "FizzBuzz",
# #                np.where(arr % 5 == 0, "Buzz",
# #                         np.where(arr % 3 == 0, "Fizz", "other")))
#
# # arr = np.where(arr < 5, "Small", np.where((5 <= arr) & (arr <= 10), "Medium", "Large"))
#
# conditions = [arr < 5, (5 <= arr) & (arr <= 10), (arr > 10) & (arr <= 20), arr > 20]
# choices = ["Small", "Medium", "Large", "XLarge"]
# arr = np.select(conditions, choices, default=None)
# print(arr)
#
#
# scores = np.array([35, 55, 67, 72, 89, 95, 100, 43, 28])
#
# conditions = [scores < 40, (scores >= 40) & (scores <= 59), (scores >= 60) & (scores <= 79), (scores >= 80) & (scores <= 100)]
# choices = ["Fail", "Pass", "Good", "Excellent"]
# result = np.select(conditions, choices, default=None)
# print(result)
#
# result = np.where(scores < 40, "Fail",
#                   np.where((scores >= 40) & (scores < 60), "Pass",
#                            np.where((scores >= 60) & (scores < 80), "Good",
#                                     np.where((scores >= 80) & (scores <= 100), "Excellent", "Unknown"))))
# print(result)
#
# salaries = np.array([25000, 45000, 60000, 82000, 120000, 500000])
#
# conditions = [salaries < 30000, (salaries >= 30000) & (salaries < 60000), (salaries >= 60000) & (salaries <= 100000), salaries > 100000]
# choices = [1, 2, 3, 4]
# result = np.select(conditions, choices, default=None)
# print(result)
#
# # np.vectorize wraps a normal python function and applies it to each element sequentially
# # for example we look up a value in a map using key map[key] but we can't lookup a list of values together
#
# mapping = {1: "Low", 2: "Mid", 3: "High"}
# vectorized_lookup = np.vectorize(mapping.get)
# lis = np.array([1, 2, 3, 4])
# print(vectorized_lookup(lis))  # not always faster than a loop, still calls python under the hood
#
#
# def classify(x):
#     if x < 13:
#         return "Child"
#     elif (x >= 13) and (x < 20):
#         return "Teen"
#     elif (x >= 20) and (x < 60):
#         return "Adult"
#     else:
#         return "Senior"
#
#
# ages = np.array([5, 15, 30, 70, 19, 60])
#
# categorize = np.vectorize(classify)
# print(categorize(ages))

"""
💡 Key difference in practice:

If you had hundreds of thresholds (say, income slabs for every ₹5000), writing conditions with np.select would be a nightmare. With digitize, you just pass the bin edges.

digitize also makes the intent super clear → “I’m bucketing values into bins.”

🔑 Interview takeaway:

Use np.select for explicit logical conditions.

Use np.digitize when the problem is fundamentally about binning numbers.
"""

# score_bin = [40, 60, 80, 101]
# grade = ['F', 'C', 'B', 'A']
#
# scores = np.array([35, 42, 67, 89, 55, 100, 76])
#
# scores = np.digitize(scores, score_bin)
# result = [grade[i] for i in scores]
# print(result)
#
# age_bin = [13, 20, 60, 200]
# demo = ['Child', 'Teen', 'Adult', 'Senior']
#
# ages = np.array([5, 15, 30, 70, 19, 60])
#
# indices = np.digitize(ages, age_bin)
# result = [demo[i] for i in indices]
# print(result)
#
# salary_bin = [30000, 60000, 100000, 200000, 1500000]
# bracket = ['Low', 'Mid', 'High', 'Very High', "What the hell are you gonna do with all that money?"]
#
# incomes = np.array([15000, 45000, 60000, 120000, 220000, 1000000])
#
# indice = np.digitize(incomes, salary_bin, right=True)
# result = np.array(bracket)[indice]
# print(result)

# # Mean
# nums = np.array([2, 7, 4, 9, 23, 98, 0, 3])
# print(np.mean(nums))
# print(nums.mean())  # same
#
# # axis wise mean: Axis 0 - column wise, Axis 1 = row wise
# nums = np.array([
#     [0, 8, 6],
#     [1, 0, 3],
#     [4, 5, 0]
# ])
#
# print(np.mean(nums, axis=0))
# print(np.mean(nums, axis=1))
#
# # Median value when sorted. If even number of values then average of middle two, axis wise too
# print(np.median(nums))
#
# # Standard deviation and variance - axis wise too
# print(np.std(nums))
# print(np.var(nums))
#
# # Sum, Min, Max - axis wise too
# print(np.sum(nums))
# print(np.min(nums))
# print(np.max(nums))
#
# # argmin and argmax for array and matrix -axis wise too. Gives index of min/max value
#
# print(np.argmax(nums), np.argmin(nums))
# # axis gives row by row or column by column index
#
# # cumulative sum and product - axis wise too
#
# # print(np.cumsum(nums, axis=1))
# # print(np.cumprod(nums, axis=1))
#
# # non zero return indices of non zero element
# indices = np.nonzero(nums)
# print(nums[indices])
# # print(indices)
#
# # fancy indexing in basic array
# arr = np.array([10, 20, 30, 40, 50])
#
# # Pick elements by index positions
# print(arr[[0, 2, 4]])  # [10 30 50]
#
# # Reordering
# print(arr[[4, 2, 0]])  # [50 30 10]
#
# # Repeated indices
# print(arr[[1, 1, 3]])  # [20 20 40]
#
# mat = np.array([[10, 20, 30],
#                 [40, 50, 60],
#                 [70, 80, 90]])
#
# # Pick specific rows
# print(mat[[0, 2]])
# # [[10 20 30]
# #  [70 80 90]]
#
# # Pick specific columns (need slicing)
# print(mat[:, [0, 2]])  # adding a colon as an arg returns columns
# # [[10 30]
# #  [40 60]
# #  [70 90]]
#
# # Pick elements at (0,0), (1,1), (2,2)
# print(mat[[0, 1, 2], [0, 1, 2]])  # [10 50 90]  # both lists would be treated as row list and column list
#
# print(mat[[0, 2], 1:])  # columns 1 onwards
#
# scores = np.array([50, 80, 30, 70, 40])
# top3_ind = np.argsort(scores)[-3:]  # np.argsort(scores) - returns sorted values indices
# print(top3_ind)
# print(scores[top3_ind])
#
# sorted_arr = np.array([0, 1, 2, 4, 5, 6, 7])
# print(np.searchsorted(sorted_arr, 3))
#
#
# # arrays are homogenous, meaning all the elements of an array have to be of the same data type
# l1 = [1, 2, 3, 4]
# l2 = [1, 2, 3, 4]
# print(l1 + l2)
#
# np_l1 = np.array(l1)
# np_l2 = np.array(l2)
# print(np_l1)  # list elements are separated by commas whereas np arrays are separated just by arrays
# np_l1 + np_l2
#
# # Initializing fixed size arrays
# np3 = np.zeros(7)  # initializes array of size 7 with zeros
# print(np3)  # dot implies the storage of floating point numbers
#
# np4 = np.ones(7, dtype=int)  # initializes array of size 7 with ones of integer type
# print(np4)
#
# np5 = np.full(5, [1, 2, 3, 4, 5])  # initializes array of size 5 with given values or one value
# print(np5)
#
# np6 = np.empty(5)  # initializes array of size 5 with garbage values until overwritten
# print(np6)
#
# np7 = np.arange(10)  # initializes array with sequential values
# print(np7)
#
# # Appending to numpy arrays
# # appending is not efficient as it creates a new array each time if we want to append multiple times
# np7 = np.append(np7, 10)
# print(np7)
# np7 = np.append(np7, [11, 12, 13])
# print(np7)
#
# # we can always append to a list and make it an array at the end to be more efficient
#
# # we can also append along a specific axis using axis = 0 for columns and 1 for rows
#
# np8 = np7[(np7 > 4) & (np7 < 12)]
# print(np8)

number = [8, 9, 9, 1, 6, 9, 5, 7, 3, 9, 7, 3, 4, 8, 3, 5, 8, 4, 8, 7, 5, 7, 3, 6, 1, 2, 7, 4, 7, 7, 8, 4, 3, 4, 2, 2, 2, 7, 3, 5, 6, 1, 1, 3, 2, 1, 1, 7, 7, 1, 4, 4, 5, 6, 1, 2, 7, 4, 5, 8, 1, 4, 8, 6, 2, 4, 3, 7, 3, 6, 2, 3, 3, 3, 2, 4, 6, 8, 9, 3, 9, 3, 1, 8, 6, 6, 3, 3, 9, 4, 6, 4, 9, 6, 7, 1, 2, 8, 7, 8, 1, 4]
price = [195, 225, 150, 150, 90, 60, 75, 255, 270, 225, 135, 195, 30, 15, 210, 105, 15, 30, 180, 60, 165, 60, 45, 225, 180, 90, 30, 210, 150, 15, 270, 60, 210, 180, 60, 225, 150, 150, 120, 195, 75, 240, 60, 45, 30, 180, 240, 285, 135, 165, 180, 240, 60, 105, 165, 240, 120, 45, 120, 165, 285, 225, 90, 105, 225, 45, 45, 45, 75, 180, 90, 240, 30, 30, 60, 135, 180, 15, 255, 180, 270, 135, 105, 135, 210, 180, 135, 195, 225, 75, 225, 15, 240, 60, 15, 180, 255, 90, 15, 150, 230, 150]

number = np.array(number)
price = np.array(price)

print(np.size(number))
print(np.sum(number))
print(np.mean(price), "mean")
print(np.max(price))
revenue = number * price
print(np.sum(revenue))
print(number[19] > number[49])
costly = price[price > np.mean(price)]
print(np.size(costly))