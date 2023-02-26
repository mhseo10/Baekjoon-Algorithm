# 6588
import sys

# 소수 리스트
max_n = 1000001
prime = [True] * max_n
end = int(max_n ** 0.5)

for i in range(2, end + 1):
    if prime[i]:
        for j in range(i+i, max_n, i):
            prime[j] = False

prime_list = set(i for i in range(2, max_n) if prime[i])

# 입력
while True:
    n = int(sys.stdin.readline().rstrip())
    
    if n == 0:
        break

    if n < 6:
        print('Goldbach\'s conjecture is wrong.')
        continue
    
    for i in prime_list:
        if n - i in prime_list:
            print(f'{n} = {i} + {n - i}')
            break
