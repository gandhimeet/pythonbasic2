"""
Write a Python program that accepts two strings and determines whether the letters in the second string are present in the first string.
Sample Input:
["python", "ypth"]
["python", "ypths"]
["python", "ypthon"]
["123456", "01234"]
["123456", "1234"]
Sample Output:
True
False
True
False
True
"""


def string_letter_check(str1, str2):
    return all([char in str1.lower() for char in str2.lower()])


print(string_letter_check("python", "ypth"))
print(string_letter_check("python", "ypths"))
print(string_letter_check("python", "ypthon"))
print(string_letter_check("123456", "01234"))
print(string_letter_check("123456", "1234"))
