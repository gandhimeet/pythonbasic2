"""
Write a Python program to count the number of carry operations for each addition problem.
According to Wikipedia " In elementary arithmetic, a carry is a digit that is transferred from one column of digits to another column of more significant digits. It is part of the standard algorithm to add numbers together by starting with the rightmost digits and working to the left. For example, when 6 and 7 are added to make 13, the "3" is written to the same column and the "1" is carried to the left".
"""


def carry_number(x, y):
    ctr = 0
    if (x == 0 and y == 0):
        return 0
    z = 0
    for i in reversed(range(10)):
        z = x % 10 + y % 10 + z
        if z > 9:
            z = 1
        else:
            z = 0
        ctr += z
        x //= 10
        y //= 10

    if ctr == 0:
        return "No carry operation."
    elif ctr == 1:
        return ctr
    else:
        return ctr


print(carry_number(786, 457))
print(carry_number(5, 6))
