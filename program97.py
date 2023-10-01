"""
Write a Python program to find the highest and lowest number from a given string of space-separated integers.
"""


def highest_lowest_num(str1):
    num_list = list(map(int, str1.split()))
    return max(num_list), min(num_list)


text = "1 4 5 77 9 0"
print("Original string:", text)
print("Highest and lowest number of the said string:", highest_lowest_num(text))
text = "-1 -4 -5 -77 -9 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:", highest_lowest_num(text))
text = "0 0"
print("\nOriginal string:", text)
print("Highest and lowest number of the said string:", highest_lowest_num(text))
