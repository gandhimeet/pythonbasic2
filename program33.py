"""
Write a Python program to compute the digit number of the sum of two given integers.
Input:
Each test case consists of two non-negative integers x and y which are separated by a space in a line.
0 <= x, y <= 1,000,000
Input two integers(a b):
5 7
Sum of two integers a and b.:
2
"""
print("Input two integers(a b): ")
a, b = map(int, input().split(" "))
print("Number of digit of a and b.:")
print(len(str(a + b)))
