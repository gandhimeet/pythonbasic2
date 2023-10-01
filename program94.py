"""
Write a Python program to find the largest product of a pair of adjacent elements from a given list of integers.
"""


def adjacent_num_product(list_nums):
    return max(a * b for a, b in zip(list_nums, list_nums[1:]))


nums = [1, 2, 3, 4, 5, 6]
print("Original list: ", nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))
nums = [1, 2, 3, 4, 5]
print("\nOriginal list: ", nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))
nums = [2, 3]
print("\nOriginal list: ", nums)
print("Largest product of the pair of adjacent elements of the said list:", adjacent_num_product(nums))
