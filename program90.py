"""
Write a Python program that replaces all but the last five characters of a string with "*" and returns the modified string.
Original String: kdi39323swe
new string: ******23swe
Original String: 12345abcdef
new string: ******bcdef
Original String: 12345
new string: 12345
"""


def new_string(str1):
    return '*' * (len(str1) - 5) + str1[-5:]


text = "kdi39323swe"
print("Original String: ", text)
print("new string: ", new_string(text))
text = "12345abcdef"
print("\nOriginal String: ", text)
print("new string: ", new_string(text))
text = "12345"
print("\nOriginal String: ", text)
print("new string: ", new_string(text))
