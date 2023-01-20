# 17427
"""
f(1)  : 1
f(2)  : 1, 2
f(3)  : 1, 3
f(4)  : 1, 2, 4
f(5)  : 1, 5

g(1)  =  1*1
g(2)  =  1*2  + 2*1
g(3)  =  1*3  + 2*1  + 3*1
g(4)  =  1*4  + 2*2  + 3*1  + 4*1
g(5)  =  1*5  + 2*2  + 3*1  + 4*1  + 5*1
g(n)  =  1*n  + 2*(n // 2) + 3*(n // 3) + ... + k(n // k) 
"""

import sys

n = int(sys.stdin.readline().strip())

result = sum([k * (n // k) for k in range(1, n+1)])
print(result)

