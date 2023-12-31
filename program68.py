"""
Write a Python program that counts the number of prime numbers that are less than a given non-negative number.
Sample Input:
(10)
(100)
Sample Output:
4
25
"""


def count_Primes_nums(n):
    ctr = 0

    for num in range(n):
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            ctr += 1

    return ctr


print(count_Primes_nums(10))
print(count_Primes_nums(100))
