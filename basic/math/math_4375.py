# 4375
import sys

nums = [int(a.rstrip()) for a in sys.stdin.readlines()]

for n in nums:
    result, i = 1, 1
    
    while result % n != 0:
        result += 10 ** i
        i += 1
        
    print(i)
