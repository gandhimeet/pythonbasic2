"""
Write a Python program to compute and print the sum of two given integers (greater or equal to zero). In the event that the given integers or the sum exceed 80 digits, print "overflow".
Input first integer:
25
Input second integer:
22
Sum of the two integers: 47
"""
print("Input first integer:")
x = int(input())
print("Input second integer:")
y = int(input())
if x >= 10 ** 80 or y >= 10 ** 80 or x + y >= 10 ** 80:
    print("Overflow!")
else:
    print("Sum of the two integers: ",x + y)
