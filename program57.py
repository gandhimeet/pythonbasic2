"""
There are 10 vertical and horizontal squares on a plane. Each square is painted blue and green. Blue represents the sea, and green represents the land. When two green squares are in contact with the top and bottom, or right and left, they are said to be ground. The area created by only one green square is called "island". For example, there are five islands in the figure below.
Write a Python program to read the mass data and find the number of islands.
Input:
Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros
1100000111
1000000111
0000000111
0010001000
0000011100
0000111110
0001111111
1000111110
1100011100
1110001000
Number of islands:
5
"""

c = 0


def f(x, y, z):
    if 0 <= y < 10 and 0 <= z < 10 and x[z][y] == '1':
        x[z][y] = '0'
        for dy, dz in [[-1, 0], [1, 0], [0, -1], [0, 1]]: f(x, y + dy, z + dz)


print("Input 10 rows of 10 numbers representing green squares (island) as 1 and blue squares (sea) as zeros")
while 1:
    try:
        if c: input()
    except:
        break
    x = [list(input()) for _ in [0] * 10]
    c = 1;
    b = 0
    for i in range(10):
        for j in range(10):
            if x[j][i] == '1':
                b += 1;
                f(x, i, j)
    print("Number of islands:")
    print(b)
