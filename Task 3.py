# def isPrime(num):
#     counter = abs(num) // 2
#     if (counter == 1):
#         return True
#     while (counter > 1):
#         if (num % counter == 0):
#             return False
#         counter -= 1
#     return True
#

days = int(input())
numbers = list(map(int, input().split()))

# print(numbers)

# print(numbers[::2])  # +
# print(numbers[1::2])  # -

min_pos = min(numbers[::2])
max_neg = max(numbers[1::2])

summ = sum(numbers[::2]) - sum(numbers[1::2])
# print('summ =', summ)

if (max_neg > min_pos):
    print(summ - 2 * min_pos + 2 * max_neg)
else:
    print(summ)
