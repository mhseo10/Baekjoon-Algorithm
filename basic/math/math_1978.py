# 1978
import sys

# 소수 리스트
m_n = 1000
prime = [True] * m_n
m = int(m_n ** 0.5)

for i in range(2, m + 1):
    if prime[i]:
        for j in range(i+i, m_n, i):
            prime[j] = False

prime_list = [i for i in range(2, m_n) if prime[i]]

# 입력
result = 0
n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for e in lst:
    if e in prime_list:
        result += 1

print(result)
