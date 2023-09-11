"""
Arrange integers (0 to 99) as narrow hilltop, as illustrated in Figure 1. Reading such data representing huge, when starting from the top and proceeding according to the next rule to the bottom. Write a Python program that compute the maximum value of the sum of the passing integers.
Input:
A series of integers separated by commas are given in diamonds. No spaces are included in each line. The input example corresponds to Figure 1. The number of lines of data is less than 100 lines.
Output:
The maximum value of the sum of integers passing according to the rule on one line.
Input the numbers (ctrl+d to exit):
8
4, 9
9, 2, 1
3, 8, 5, 5
5, 6, 3, 7, 6
3, 8, 5, 5
9, 2, 1
4, 9
8
Maximum value of the sum of integers passing according to the rule on one line.
64
"""

import sys
print("Input the numbers (ctrl+d to exit):")
nums = [list(map(int, l.split(","))) for l in sys.stdin]
mvv = nums[0]

for i in range(1, (len(nums)+1)//2):
    rvv = [0]*(i+1)
    for j in range(i):
        rvv[j] = max(rvv[j], mvv[j]+nums[i][j])
        rvv[j+1] = max(rvv[j+1], mvv[j]+nums[i][j+1])
    mvv = rvv

for i in range((len(nums)+1)//2, len(nums)):
    rvv = [0]*(len(mvv)-1)
    for j in range(len(rvv)):
        rvv[j] = max(mvv[j], mvv[j+1]) + nums[i][j]
    mvv = rvv
print("Maximum value of the sum of integers passing according to the rule on one line.")
print(mvv[0])
