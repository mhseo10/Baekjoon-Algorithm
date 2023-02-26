# 1929
import sys

# 소수 리스트
max_n = 1000001
prime = [True] * max_n
end = int(max_n ** 0.5)

for i in range(2, end + 1):
    if prime[i]:
        for j in range(i+i, max_n, i):
            prime[j] = False

# 입력
m, n = map(int, sys.stdin.readline().split())

m = 2 if m == 1 else m
prime_list = [i for i in range(m, n+1) if prime[i]]

for i in prime_list:
    print(i)
