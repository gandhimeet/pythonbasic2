"""
Write a Python program to compute the sum of the three lowest positive numbers from a given list of numbers.
Original list of numbers: [10, 20, 30, 40, 50, 60, 7]
Sum of the three lowest positive numbers of the said array: 37
Original list of numbers: [1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6
Original list of numbers: [0, 1, 2, 3, 4, 5]
Sum of the three lowest positive numbers of the said array: 6
"""


def sum_three_smallest_nums(lst):
    return sum(sorted([x for x in lst if x > 0])[:3])


nums = [10, 20, 30, 40, 50, 60, 7]
print("Original list of numbers: ", nums)
print("Sum of the three lowest positive numbers of the said array: ", sum_three_smallest_nums(nums))
nums = [1, 2, 3, 4, 5]
print("\nOriginal list of numbers: ", nums)
print("Sum of the three lowest positive numbers of the said array: ", sum_three_smallest_nums(nums))
nums = [0, 1, 2, 3, 4, 5]
print("\nOriginal list of numbers: ", nums)
print("Sum of the three lowest positive numbers of the said array: ", sum_three_smallest_nums(nums))
