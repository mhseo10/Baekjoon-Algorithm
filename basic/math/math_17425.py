# 17425
"""
g(1) = f(1)
g(2) = f(1) + f(2)
g(3) = f(1) + f(2) + f(3)
...
g(n) = g(n - 1) + f(n)
"""

import sys

# dynamic programming
MAX = 1000001
f, g = [1] * MAX, [0] * MAX

for i in range(2, MAX):
    for j in range(i, MAX, i):
        f[j] += i  # i의 배수에 i를 모두 더함

for i in range(1, MAX):
    g[i] = g[i - 1] + f[i]  # g(n) = g(n - 1) + f(n)

n = int(sys.stdin.readline().strip())
for i in range(n):
    query = int(sys.stdin.readline().strip())
    print(g[query])
