"""
while True:
    print("Input number of rows/columns (0 to exit)")
    n = int(input())
    if n == 0:
        break
    print("Input cell value:")
    x = []
    for i in range(n):
        x.append([int(num) for num in input().split()])

    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x[i][j]
        x[i].append(sum)

    x.append([])
    for i in range(n + 1):
        sum = 0
        for j in range(n):
            sum += x[j][i]
        x[n].append(sum)
    print("Result:")
    for i in range(n + 1):
        for j in range(n + 1):
            print('{0:>5}'.format(x[i][j]), end="")
        print()

"""


def check_sum(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == k:
                return True
    return False


print(check_sum([12, 5, 0, 5], 10))
print(check_sum([20, 20, 4, 5], 40))
print(check_sum([1, -1], 0))
print(check_sum([1, 1, 0], 0))
