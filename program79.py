"""
Write a Python program to compute the largest product of three integers from a given list of integers.
Sample Input:
[-10, -20, 20, 1]
[-1, -1, 4, 2, 1]
[1, 2, 3, 4, 5, 6]
Sample Output:
4000
8
120
"""


def largest_product_of_three(nums):
    max_val = nums[1]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                max_val = max(nums[i] * nums[j] * nums[k], max_val)

    return max_val


print(largest_product_of_three([-10, -20, 20, 1]))
print(largest_product_of_three([-1, -1, 4, 2, 1]))
print(largest_product_of_three([1, 2, 3, 4, 5, 6]))
