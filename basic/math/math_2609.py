# 2609
import sys

a, b = map(int, sys.stdin.readline().split())

# Euclidean algorithm
lcm = a * b
gcd = b

while a % b != 0:
    gcd = a % b
    a, b = b, gcd

lcm = lcm // gcd

print(gcd)
print(lcm)

# from math import sqrt
#
# prime = [True] * (a + 1) if a > b else [True] * (b + 1)
# max_len = len(prime)
# sqrt_len = int(sqrt(max_len))
# gcd, lcm = 1, 1
#
# for i in range(2, sqrt_len + 1):
#     if prime[i]:
#         for j in range(i + i, max_len, i):
#             prime[j] = False
#
# p_list = [i for i in range(2, max_len) if prime[i]]
#
# for p in p_list:
#     exp_a, exp_b = 0, 0
#
#     while a % p == 0 or b % p == 0:
#         if a % p == 0:
#             a = a // p
#             exp_a += 1
#
#         if b % p == 0:
#             b = b // p
#             exp_b += 1
#
#     gcd *= (p ** exp_a) if exp_a < exp_b else (p ** exp_b)
#     lcm *= (p ** exp_a) if exp_a > exp_b else (p ** exp_b)
#
# print(gcd)
# print(lcm)

