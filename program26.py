"""
Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).
Sample array: [1, 2, 3]
Then all the distinct pairs will be:
1 2
1 3
2 3
"""


def sum_distinct_pairs(arr):
    result = 0
    i = 0
    while i < len(arr):
        result += i * arr[i] - (len(arr) - i - 1) * arr[i]
        i += 1
    return result


print(sum_distinct_pairs([1, 2, 3]))
print(sum_distinct_pairs([1, 4, 5]))
